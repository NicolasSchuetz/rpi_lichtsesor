# TSL2591 Sensor Data Logger

This Python script interfaces with the Adafruit TSL2591 light sensor to measure and log light data, including lux, infrared, visible, and full spectrum readings. The data is saved into a `CSV` file for analysis.

## Features
- Records lux, infrared, visible, and full spectrum light data.
- Logs data to `sensor.csv` with timestamps in UTC format.
- Automatically appends new data to the CSV file on each run.

## Requirements
- [Adafruit CircuitPython](https://circuitpython.org/)
- `adafruit-circuitpython-tsl2591` library
- A device with I2C support (like a Raspberry Pi)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tsl2591-sensor-logger.git
2. Install the necessary dependencies:
   pip install adafruit-circuitpython-tsl2591
3. Run the script:
   python sensor_logger.py

