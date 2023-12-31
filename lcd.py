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

def display_error():
    lcd.clear()
    lcd.putstr("Unknown error")
    lcd.move_to(0,1)
    lcd.putstr("Please reboot")