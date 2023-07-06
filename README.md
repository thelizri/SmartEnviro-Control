* Project Maker: William Carlstedt
* Student Credentials: wc222br

This tutorial offers step-by-step guidance to set up a temperature and humidity sensor that displays these metrics on an LCD display, and a desk fan that turns on automatically when the temperature goes above a certain threshold.

This project can be finished in a few hours you have all the required materials. Maybe a few evenings if you're completely new to IoT.

## Objective

The primary motivation behind the SmartEnviro-Control project was to enhance the comfort of my workspace, particularly during the summer. I often turn on the fan when it gets too hot and it gets quite annoying. I found myself thinking that it would be nice if the fan would turn on itself when it gets too hot, so I don't have to do it myself. 

This project serves two major purposes:

1. **Practical Comfort**: It's designed to maintain an optimal environment at my workspace by providing real-time temperature and humidity readings and automatically controlling a desk fan based on these values. This way, it ensures a comfortable workspace environment without any manual intervention, which is especially useful during hot summer days.

2. **Educational Insight**: Beyond its practical application, this project offers a valuable learning journey for any beginner programmers into the world of IoT. It will provide you with some rudimentary experience with microcontrollers, sensors, actuators, and the MQTT protocol. It provides a hands-on experience in IoT system design and gives insights into the integration of hardware components and programming them to work cohesively.


## Material


| Hardware | Description | Price and Link | Picture |
| -------- | -------- | -------- | -------- |
| Raspberry Pi Pico W     | Microcontroller for the project   | [109 kr](https://www.electrokit.com/produkt/raspberry-pi-pico-wh/)     | ![](https://hackmd.io/_uploads/ry6wHK4t3.jpg) |
| DHT11   | Temperature and humidity sensor     | [49 kr](https://www.electrokit.com/produkt/digital-temperatur-och-fuktsensor-dht11/)     | ![dht11](https://hackmd.io/_uploads/rJl5HFVth.jpg) |
| 5V Relay Module     | Used to turn on desk fan     | [39 kr](https://www.electrokit.com/produkt/relamodul-5v/)     | ![relay](https://hackmd.io/_uploads/S1thHFEt3.jpg) |
| 2x16 LCD Display     | Used to display temperature and humidity     | [99 kr](https://www.electrokit.com/produkt/lcd-2x16-tecken-jhd162a-stn-gulgron-led/)     | ![](https://hackmd.io/_uploads/SkrkIYEK2.jpg) |
| I2C-Interface    | Interface for the LCD display. Makes it easier to connect everything.     | [39 kr](https://www.electrokit.com/produkt/i2c-interface-for-lcd/)     | ![i2c](https://hackmd.io/_uploads/ByE-8FVK3.jpg) |
| Micro USB Cable | Needed to connect Pico W to computer| [39 kr](https://www.electrokit.com/en/product/usb-cable-a-male-microb-male-1-8m/) | ![](https://hackmd.io/_uploads/rJHEwtEFh.jpg) | 
| Generic Desk Fan | Desk fan | [199 kr](https://www.kjell.com/se/produkter/hem-fritid/flaktar-ac/bordsflaktar/rubicson-bordsflakt-o23-cm-p47013) | ![](https://hackmd.io/_uploads/H1PFUF4Y2.jpg) |

  
| Miscellaneous Materials | Price and Link | Picture |
| -------- | -------- | -------- |
| Jumper Wires Female/Male| [29 kr](https://www.electrokit.com/en/product/jumper-wires-20-pin-30cm-female-male/)     | ![](https://hackmd.io/_uploads/HyOxDtNK2.jpg) |
| Jumper Wires Male/Male| [29 kr](https://www.electrokit.com/en/product/jumper-wires-20-pin-30cm-male-male/)     | ![](https://hackmd.io/_uploads/r1QGwFEY2.jpg) |
| Solderless Breadboard | [69 kr](https://www.electrokit.com/en/product/solderless-breadboard-840-tie-points-2/) | ![](https://hackmd.io/_uploads/B1ImPtVY3.jpg) |

## Computer Setup

### Installing MicroPython on Pico W

1. Download the MicroPython uf2 file from [here](https://micropython.org/download/rp2-pico-w/).
2. Connect your Raspberry Pi Pico W to your computer via USB while holding down the BOOTSEL button.
3. Once the device appears as a USB mass storage device, drag and drop the uf2 file onto it.
4. The device will automatically reset and be ready for use once the firmware has flashed.

### Installing Thonny IDE

1. Download and install the Thonny IDE suitable for your OS from [here](https://thonny.org/).
2. Connect the Pico W to your computer via USB.
3. In Thonny, go to Tools > Options and select Interpreter.
4. From the dropdown menu, select the MicroPython interpreter for Raspberry Pi Pico.

### Uploading Code to Pico W

1. Open Thonny
2. Access the Pico's file system: Click on the "View" menu at the top, then select "Files". This will open a new section in Thonny that allows you to see the files on your Pico and your computer.
3. Transfer Files: In the "Files" section, you'll see two panes - "This computer" and "MicroPython device". Navigate to the file on your computer that you want to copy to the Pico. Then, simply drag and drop the file from the "This computer" pane to the "MicroPython device" pane. The file should now be copied over to your Pico.

## Putting Everything Together

First connect the I2C interface to the Raspberry Pi Pico on the breadboard. It should look something similar to this (but without the cables):

![i2c](https://hackmd.io/_uploads/SJbsINGY2.jpg)

Next, you'll need to configure the power cable of your desk fan to connect with the relay. Take one of the wires within the power cable and sever it. Once it's cut, strip the ends and attach them to the relay. When done correctly, it should resemble something like this (ignore the glue. I just added that for extra reinforcement. It's not necessary!):

![relay](https://hackmd.io/_uploads/HkY5PNzKn.jpg)

Then finish by connecting everything that's left according to this wiring diagram: 

![wiring-diagram](https://hackmd.io/_uploads/rkRYNtVth.png)


The relay's signal wire is connected to GPIO 15 and the DHT11's signal wire is connected to GPIO 16. The LCD display gets its power from the VBUS on the Pico because it needs 5 volts instead of 3 volts. You can find more information about the pinout of the Pico [here](https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf).

## Platform

In this project, we require an IoT platform to house our project and manage the data it produces. IoT platforms offer user-friendly solutions for connecting, managing, and visualizing data from your IoT devices. Among these, Ubidots, Adafruit IO, and Datacake are widely used. However, for this project, I chose to use Adafruit IO for several reasons:

* User-friendly interface: Adafruit IO is quite simple to navigate, making it ideal for beginners or smaller, DIY projects.
* Real-time data streaming: This platform provides real-time data streaming and dashboards that can be customized to your needs.
* API Support: It supports MQTT and REST APIs, which are useful for managing data.
* Cost-effective: Adafruit IO is free to use up to 30 messages per minute. They also offer a paid plan for more extensive use.

## The Code

All code can be found at my GitHub [repository](https://github.com/thelizri/SmartEnviro-Control/blob/main/main.py). I encourage you to try to write some of the code yourself and not just copy everything completely. You will learn a lot more that way.

### Connecting to WiFi

I didn't write this function myself. I got it from this [link](https://hackmd.io/@lnu-iot/r1yEtcs55). But here's a short explanation of what it does: The Python function `do_connect()` serves to establish a Wi-Fi connection using the network interface of the device. Initially, it imports necessary modules: `network` for networking-related operations and `time` to use sleep for delay. It sets the network interface to the Station mode, which allows the device to connect to a Wi-Fi network. The function checks if the device is already connected to a network using the `isconnected()` method. If it's not already connected, it activates the network interface and adjusts the power mode to disable Wi-Fi power-saving (a step that might not be necessary for all devices). Subsequently, it attempts to connect to a specified Wi-Fi network using the SSID and password. While trying to establish the connection, it enters a loop where it checks every second if a successful connection has been made while ensuring the WLAN interface status is positive, indicating no errors. Once the connection is successful, it prints and returns the IP address assigned by the router to the device.

```
def do_connect():
    import network
    from time import sleep

    wlan = network.WLAN(network.STA_IF)  # Put modem on Station mode

    if not wlan.isconnected():  # Check if already connected
        print("connecting to network...")
        wlan.active(True)  # Activate network interface
        # set power mode to get WiFi power-saving off (if needed)
        wlan.config(pm=0xA11140)
        wlan.connect(WIFI_SSID, WIFI_PASS)  # Your WiFi Credential
        print("Waiting for connection...", end="")
        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print(".", end="")
            sleep(1)
    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print("\nConnected on {}".format(ip))
    return ip
```

### Connecting to Adafruit IO

The code for the MQTT client comes from this [repository](https://github.com/iot-lnu/applied-iot/tree/master).This script uses MQTT to connect to Adafruit IO. After creating an MQTT client, it sets a callback function for received messages. It then connects to the server and subscribes to two feeds: one for the desk fan and one for temperature threshold. It also publishes initial messages to these feeds: the current temperature threshold and a command to turn the desk fan on. A confirmation message is printed to indicate successful connection and subscription.

```
# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)

# Subscribed messages will be delivered to this callback
client.set_callback(sub_cb)
client.connect()
client.subscribe(AIO_DESK_FAN_FEED)
client.subscribe(AIO_TEMPERATURE_THRESHOLD_FEED)
client.publish(topic=AIO_TEMPERATURE_THRESHOLD_FEED, msg=str(TEMPERATURE_THRESHOLD))
client.publish(topic=AIO_DESK_FAN_FEED, msg="ON")
print("Connected to %s, subscribed to %s topic and %s topic" % (AIO_SERVER, AIO_DESK_FAN_FEED, AIO_TEMPERATURE_THRESHOLD_FEED))
```

### Publishing Values to Adafruit IO

This section of code utilizes the established MQTT client to publish temperature and humidity readings to Adafruit IO. It does this by targeting the appropriate feeds, essentially 'tags' for organizing the data. The `send_temperature` and `send_humidity` functions each take a value (temperature or humidity), print a message indicating what they are about to publish, and then attempt to publish this value to the corresponding feed on Adafruit IO. If successful, a "DONE" message is printed. If the publish attempt fails due to any exceptions, it prints "FAILED".

```
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
```

### Callback Functions

Sure. This code handles incoming messages from Adafruit IO feeds. The function `sub_cb()` gets triggered when a message arrives. If the topic of the message contains 'desk_fan', it calls the `enable_fan()` function which, depending on the message content, toggles the fan and the onboard LED on the Raspberry Pi Pico on or off. The LED is not necessary, but it makes it easy to see when desk fan is turned on or not. If the topic contains 'temperature-threshold', it triggers the `change_temp_threshold()` function which updates a global temperature threshold value. This way, the fan's behavior and the temperature limit can be controlled remotely.

```
# Callback Function to respond to messages from Adafruit IO
def sub_cb(topic, msg):  # sub_cb means "callback subroutine"
    topic = str(topic)
    print((topic, msg))  # Outputs the message that was received. Debugging use.
    if 'desk_fan' in topic:
        enable_fan(msg)
    elif 'temperature-threshold' in topic:
        change_temp_threshold(msg)


def enable_fan(msg):
    global TURNED_ON
    if msg == b"ON":  # If message says "ON" ...
        TURNED_ON = True
        LED.on()  # ... then LED on
    elif msg == b"OFF":  # If message says "OFF" ...
        TURNED_ON = False
        LED.off()  # ... then LED off
        turn_off_fan()
    else:  # If any other message is received ...
        print("Unknown message")  # ... do nothing but output that it happened.

def change_temp_threshold(msg):
    global TEMPERATURE_THRESHOLD
    TEMPERATURE_THRESHOLD = int(msg)
```

### Reading from Sensor

This code is used to interact with the DHT11 temperature and humidity sensor. The `dht.DHT11(machine.Pin(16))` line initializes a DHT11 sensor connected to GPIO pin 16. The `get_temperature_and_humidity()` function prompts the DHT11 sensor to take a measurement using `TEMP_HUMIDITY_SENSOR.measure()`, then retrieves the temperature and humidity values from the sensor with `TEMP_HUMIDITY_SENSOR.temperature()` and `TEMP_HUMIDITY_SENSOR.humidity()`, respectively. The function then returns these values.

```
import dht

TEMP_HUMIDITY_SENSOR = dht.DHT11(machine.Pin(16))  # DHT11 Constructor

# Returns the temperature in celsius and the humidity
def get_temperature_and_humidity():
    TEMP_HUMIDITY_SENSOR.measure()
    temperature = TEMP_HUMIDITY_SENSOR.temperature()
    humidity = TEMP_HUMIDITY_SENSOR.humidity()
    return temperature, humidity
```

### Turning on the Fan

This code manages the operation of a desk fan through a relay connected to GPIO pin 15. The initial line `FAN = Pin(15, Pin.OUT)` sets up pin 15 as an output pin. The `FAN.value(1)` line sets this pin to HIGH, which opens the relay and turns off the fan.

The `turn_on_fan()` function sets the pin to LOW with `FAN.value(0)`, closing the relay and thereby powering on the fan. Conversely, the `turn_off_fan()` function sets the pin back to HIGH, opening the relay and switching off the fan.

```
FAN = Pin(15, Pin.OUT)
FAN.value(1)

def turn_on_fan():
    FAN.value(0)


def turn_off_fan():
    FAN.value(1)
```

### LCD Display

For communication with the LCD display, I am utilizing an external library available at this [link](https://github.com/T-622/RPI-PICO-I2C-LCD). This library significantly simplifies the interaction with the LCD display, sparing us the need to create the drivers manually. The code snippet provided below is relatively straightforward. Its function is twofold: (1.) initialize the display and, (2.) output the current temperature and humidity readings to the display.

```
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.clear()
lcd.putstr("Starting")

def update_display(temperature, humidity):
    lcd.clear()
    lcd.putstr(str(round(temperature, 1))+" Celsius")
    lcd.move_to(0, 1)
    lcd.putstr(str(round(humidity))+"% Humidity")
```

## Transmitting the Data

In this SmartEnviro-Control project, data transmission occurs via WiFi and the MQTT protocol. 

1. **Frequency of Transmission**: The data, specifically temperature and humidity readings, is transmitted every 60 seconds to ensure real-time monitoring and control of the workspace environment.

2. **Choice of Wireless Protocol - WiFi**: I chose to use WiFi for wireless communication for its convenience and reliability within a limited range. Given that the device will always be situated on my desk, WiFi provides a stable connection with high data transmission rates, enabling a smooth, real-time update of sensor readings.

3. **Transport Protocol - MQTT**: The MQTT (Message Queuing Telemetry Transport) protocol was chosen for data transmission to the Adafruit IO platform. This lightweight messaging protocol is designed for constrained devices and low-bandwidth, high-latency networks, making it an excellent choice for IoT applications. It creates an easy way for real-time data streaming and visualization.

## Presenting the Data

Here's a glimpse of the user interface on Adafruit IO. The dashboard comprises two blocks that displays the real-time values of the current temperature and humidity. There's also a toggle button to manually control the fan and a slider that lets you tweak the temperature threshold as needed.

Furthermore, it features two line charts that illustrate the change in temperature and humidity over a period of time, providing an overview of the environmental trends.

The data, diligently recorded every minute by the Pi Pico, is seamlessly uploaded to the database, enabling real-time environmental monitoring. Data for each feed is stored for 30 days.

![Dashboard](https://hackmd.io/_uploads/Syqv2lXY3.png)

## Finalizing the Design

![lcd-breadboard](https://hackmd.io/_uploads/H1dBAl7K3.jpg)

![sensor-breadboard](https://hackmd.io/_uploads/BJx8AgXYh.jpg)

![relay-deskfan](https://hackmd.io/_uploads/rJDI0lXt2.jpg)

The SmartEnviro-Control project in its current form is functional, yet there's ample scope for enhancement. We could refine its aesthetics by 3D printing a customized enclosure to neatly house all the components.

Moreover, the code could undergo refactoring to enhance performance and efficiency. Additional functionalities can be incorporated like adding a Passive Infrared (PIR) sensor to detect motion. For instance, a detected movement in the morning could trigger the system to switch on the computer automatically, adding another layer of convenience to your workspace.

As you can see, the possibilities for improvement and customization are vast and limited only by your creativity!

