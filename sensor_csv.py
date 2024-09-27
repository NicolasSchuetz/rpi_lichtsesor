import time
import board
import adafruit_tsl2591
from datetime import timezone 
import datetime 
import os

if os.path.exists("sensor.csv")==False:
    file=open("sensor.csv","a")
    file.write("Time,Lux,Infrared,Visible,Full_Spectrum\n")
else:
    file=open("sensor.csv","a")



def gettime(): 
    dt = datetime.datetime.now(timezone.utc) 
    utc_time = dt.replace(tzinfo=timezone.utc) 
    utc_timestamp = utc_time.timestamp() 
    return utc_timestamp

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  

# Initialize the sensor.
sensor = adafruit_tsl2591.TSL2591(i2c)

while True:
    try:
        # Read and calculate the light level in lux.
        lux = sensor.lux
        # IR-only levels range from 0-65535 (16-bit)
        infrared = sensor.infrared
        # Visible-only levels range from 0-2147483647 (32-bit)
        visible = sensor.visible
        # Full spectrum (visible + IR) also range from 0-2147483647 (32-bit)
        full_spectrum = sensor.full_spectrum
        time.sleep(4.0)
        print(lux)
    except Exception as ex:
        print(ex)
    except KeyboardInterrupt:
        file.close()
        break

