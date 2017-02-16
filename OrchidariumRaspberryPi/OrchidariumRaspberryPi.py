import ptvsd
ptvsd.enable_attach('xplatdemo')
#xplatdemo@192.168.0.104

import time
import serial
import json

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
            ser.write(sendMessage)
            print("sending sync message")
        except:
            print("error writing time")
    else:
        #data = json.loads(newLine)
        print('loaded data')
        #print(data['tempF'])
        #parse sensor data

#ser.open()
while True:
    newLine = ser.readline()
    if newLine:
        reactToNewLine(newLine)

#str(int(time.time()+TimeZone))
