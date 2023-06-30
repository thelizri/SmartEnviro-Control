# Project Name: SmartEnviro-Control

## Description

SmartEnviro-Control is an IoT-based environment monitoring and control system designed to optimize your personal workspace comfort. Powered by a Raspberry Pi Pico W, the system uses a DHT11 sensor to constantly measure the ambient temperature and humidity. Upon reaching a predefined temperature threshold, a relay triggers a desk fan for active cooling. The system simultaneously provides real-time temperature and humidity readings through a 2x16 LCD display for easy monitoring. Additionally, the collected data is uploaded to Adafruit IO for online tracking and analysis.

## Hardware Components

- [Raspberry Pi Pico W](https://www.electrokit.com/produkt/raspberry-pi-pico-wh/)
- [DHT11 Temperature and Humidity Sensor](https://www.electrokit.com/produkt/digital-temperatur-och-fuktsensor-dht11/)
- [5V Relay Module](https://www.electrokit.com/produkt/relamodul-5v/)
- Generic Desk Fan
- [2x16 LCD Display](https://www.electrokit.com/produkt/lcd-2x16-tecken-jhd162a-stn-gulgron-led/)
- [I2C Interface for LCD](https://www.electrokit.com/produkt/i2c-interface-for-lcd/)

## Installation

*Note: This guide assumes that you have already setup your Raspberry Pi Pico with MicroPython.*

1. Connect the DHT11 sensor and the relay to your Raspberry Pi Pico as per the included wiring diagram.
2. Connect the fan to the relay and the LCD display to the Pico via the I2C interface as per the included wiring diagram.
3. Clone the repository and upload the .py files to your Raspberry Pi Pico.

## Software Dependencies

This project uses the following MicroPython libraries:

- `dht`
- `machine`
- `utime`
- `RPI-PICO-I2C-LCD` (found [here](https://github.com/T-622/RPI-PICO-I2C-LCD))
- `mqtt`
- `ubinascii`

## Usage

1. Replace all the blanks in secrets.py with your credentials
2. Power on the Raspberry Pi Pico.
3. The LCD display will show the current temperature and humidity levels.
4. The fan will activate automatically when the temperature exceeds the predefined threshold.
5. The system data will be pushed to your Adafruit IO account.

## Wiring
![Wiring Diagram](https://github.com/thelizri/SmartEnviro-Control/blob/main/Wiring/Wiring_bb.png)
