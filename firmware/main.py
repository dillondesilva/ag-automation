import requests.packages.urllib3
import serial
import requests
import json
import RPI.GPIO as GPIO
from datetime import datetime as dt

requests.packages.urllib3.disable_warnings()

ser = serial.Serial('/dev/ttyUSB0', 9600)

# moisture_val takes the analog value and returns a number between
# 0 - 100 representing a percentage
def moisture_val(analog_val):
        return float(float(analog_val)/1023) * 100

while True:
        # Reading line from serial and extracting necessary information
        val = moisture_val(ser.readline())
        datetime = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        http_put_data = {"testing": {"lastSync": datetime, "value": val}}

        # Putting our data in firebase
        r = requests.put('$(INSERT_DATABASE_URL', data=json.dumps(http_put_data))
        print(val)