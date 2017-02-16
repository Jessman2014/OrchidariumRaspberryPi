import ptvsd
ptvsd.enable_attach('xplatdemo')
#xplatdemo@192.168.0.104

import time
import datetime
import serial
import json
import requests

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 9600
)

TIME_HEADER = "T"
TIME_REQUEST = 7

def reactToNewLine(newLine):
    newLine = newLine.decode("utf-8").strip()
    if (newLine == "waiting for sync message"):
        try:
            sendMessage = TIME_HEADER + str(int(time.time()))
            ser.write(sendMessage.encode("utf-8"))
            print("sending sync message")
        except Exception as inst:
            print("error writing time")
            print(type(inst))     # the exception instance
    else:
        print('loaded data')
        #data = json.loads(newLine)
        #data['Id'] = 0
        #data['SoilMoisture'] = 0
        #data['DateAdded'] = str(datetime.datetime.now())
        #print(data['TemperatureF'])
        #print(data['Humidity'])
        #r = requests.post('http://plantwatcherbot.azurewebsites.net/api/SensorReadings', data = data)
        #print(data['dateRecorded'])
#parse sensor data

#ser.open()
while True:
    newLine = ser.readline()
    if newLine:
        reactToNewLine(newLine)

#str(int(time.time()+TimeZone))
