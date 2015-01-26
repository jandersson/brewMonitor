import serial
import json
from time import localtime, strftime

brewname = "My Brown Nuts"
f = open('workfile', 'w')
ser = serial.Serial('/dev/ttyACM0', 9600)
datapoint = {'temperature': None,
             'timestamp': None,
             'brewname': brewname}

while True:
    datapoint['temperature'] = ser.readline()
    datapoint['timestamp'] = strftime("%Y-%m-%d %H:%M:%S", localtime())

f.close()
ser.close()
