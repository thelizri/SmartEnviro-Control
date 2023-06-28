import time  # Allows use of time.sleep() for delays
from mqtt import MQTTClient  # For use of MQTT protocol to talk to Adafruit IO
import ubinascii  # Conversions between binary data and various encodings
import machine  # Interfaces with hardware components
import micropython  # Needed to run any MicroPython code
import random  # Random number generator
from machine import Pin, time_pulse_us  # Define pin
import dht
import lcd
from secrets import *


# BEGIN SETTINGS
# These need to be change to suit your environment
MEASUREMENT_INTERVAL = 10000
TURNED_ON = True
last_measurement = 0
led = Pin("LED", Pin.OUT)  # led pin initialization for Raspberry Pi Pico W
led.on()
tempSensor = dht.DHT11(machine.Pin(16))  # DHT11 Constructor
fan = Pin(15, Pin.OUT)
fan.value(1)

AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything

# END SETTINGS


# FUNCTIONS


# Function to connect Pico to the WiFi
def do_connect():
    import network
    from time import sleep

    wlan = network.WLAN(network.STA_IF)  # Put modem on Station mode

    if not wlan.isconnected():  # Check if already connected
        print("connecting to network...")
        wlan.active(True)  # Activate network interface
        # set power mode to get WiFi power-saving off (if needed)
        wlan.config(pm=0xA11140)
        wlan.connect("WIFI_SSID", "WIFI_PASS")  # Your WiFi Credential
        print("Waiting for connection...", end="")
        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print(".", end="")
            sleep(1)
    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print("\nConnected on {}".format(ip))
    return ip


# Callback Function to respond to messages from Adafruit IO
def sub_cb(topic, msg):  # sub_cb means "callback subroutine"
    global TURNED_ON
    print((topic, msg))  # Outputs the message that was received. Debugging use.
    if msg == b"ON":  # If message says "ON" ...
        TURNED_ON = True
        led.on()  # ... then LED on
    elif msg == b"OFF":  # If message says "OFF" ...
        TURNED_ON = False
        led.off()  # ... then LED off
        turn_off_fan()
    else:  # If any other message is received ...
        print("Unknown message")  # ... do nothing but output that it happened.


# Returns the temperature in celsius and the humidity
def get_temperature_and_humidity():
    tempSensor.measure()
    temperature = tempSensor.temperature()
    humidity = tempSensor.humidity()
    return temperature, humidity


def turn_on_fan():
    fan.value(0)


def turn_off_fan():
    fan.value(1)


def send_temperature(temperature):
    print(
        "Publishing: {0} to {1} ... ".format(temperature, AIO_TEMPERATURE_FEED), end=""
    )
    try:
        client.publish(topic=AIO_TEMPERATURE_FEED, msg=str(temperature))
        print("DONE")
    except Exception as e:
        print("FAILED")


def send_humidity(humidity):
    print("Publishing: {0} to {1} ... ".format(humidity, AIO_HUMIDITY_FEED), end="")
    try:
        client.publish(topic=AIO_HUMIDITY_FEED, msg=str(humidity))
        print("DONE")
    except Exception as e:
        print("FAILED")


# Try WiFi Connection
try:
    ip = do_connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)

# Subscribed messages will be delivered to this callback
client.set_callback(sub_cb)
client.connect()
client.subscribe(AIO_LIGHTS_FEED)
print("Connected to %s, subscribed to %s topic" % (AIO_SERVER, AIO_LIGHTS_FEED))


try:  # Code between try: and finally: may cause an error
    # so ensure the client disconnects the server if
    # that happens.
    while True:  # Repeat this loop forever
        client.check_msg()  # Action a message if one is received. Non-blocking.
        temperature, humidity = get_temperature_and_humidity()
        lcd.update_display(temperature, humidity)
        if (time.ticks_ms() - last_measurement) > MEASUREMENT_INTERVAL:
            if TURNED_ON:
                if temperature > 24:
                    turn_on_fan()
                else:
                    turn_off_fan()
            send_temperature(temperature)
            send_humidity(humidity)
            last_measurement = time.ticks_ms()
            print("------------------")
        time.sleep(10)

finally:  # If an exception is thrown ...
    client.disconnect()  # ... disconnect the client and clean up.
    client = None
    print("Disconnected from Adafruit IO.")
