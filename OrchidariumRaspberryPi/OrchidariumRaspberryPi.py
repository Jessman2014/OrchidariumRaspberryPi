import ptvsd
ptvsd.enable_attach('xplatdemo')

import time
import serial

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 9600
)

TIME_HEADER = "T"
TIME_REQUEST = 7

def reactToNewLine(newLine):
    if (newLine == "waiting for sync message"):
        ser.write(TIME_HEADER + str(int(time.time())))
    else:
        print(newLine)
        #parse sensor data

#ser.open()
while True:
    newLine = ser.readline()
    if newLine:
        reactToNewLine(newLine)

#str(int(time.time()+TimeZone))
