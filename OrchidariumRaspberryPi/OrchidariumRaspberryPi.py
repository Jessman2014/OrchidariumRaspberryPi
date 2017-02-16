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
        print('loaded data: ', newLine)
        try:
            data = json.loads(newLine)
            if 'TemperatureF' in data and 'Humidity' in data:
                print('valid data')
                data['Id'] = 0
                data['SoilMoisture'] = 0
                data['DateAdded'] = str(datetime.datetime.now())
                r = requests.post('http://plantwatcherbot.azurewebsites.net/api/SensorReadings', data = data)
        except Exception as inst:
            print(type(inst))

        
        #print(data['TemperatureF'])
        #print(data['Humidity'])
        #print(data['dateRecorded'])
#parse sensor data

#ser.open()
while True:
    newLine = ser.readline() #'{"TemperatureF":69.13,"Humidity":72.84,"Lux":204.00,"FoggerOn":true,"BoilerOn":true,"MainLED":true,"SecondaryLEDs":true,"dateRecorded":1487255312}' #
    if newLine:
        reactToNewLine(newLine)

#str(int(time.time()+TimeZone))
