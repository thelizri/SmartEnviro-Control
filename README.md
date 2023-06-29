# Project Name: SmartEnviro-Control

## Description

SmartEnviro-Control is an IoT-based environment monitoring and control system designed to optimize your personal workspace comfort. Powered by a Raspberry Pi Pico W, the system uses a DHT11 sensor to constantly measure the ambient temperature and humidity. Upon reaching a predefined temperature threshold, a relay triggers a desk fan for active cooling. The system simultaneously provides real-time temperature and humidity readings through a 2x16 LCD display for easy monitoring. Additionally, the collected data is uploaded to Adafruit IO for online tracking and analysis.

## Hardware Components

- Raspberry Pi Pico W
- DHT11 Temperature and Humidity Sensor
- Relay Module
- Desk Fan
- 2x16 LCD Display
- I2C Interface for LCD

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
- `time`
- `mqtt`
- `ubinascii`

## Usage

1. Power on the Raspberry Pi Pico.
2. The LCD display will show the current temperature and humidity levels.
3. The fan will activate automatically when the temperature exceeds the predefined threshold.
4. The system data will be pushed to your Adafruit IO account.

## Contributing

Contributions are welcome! Please feel free to share improvements, bug reports, or other forms of feedback.

---