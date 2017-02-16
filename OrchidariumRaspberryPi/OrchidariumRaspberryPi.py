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
    newLine.decode("utf-8").rstrip()
    if (newLine == "waiting for sync message"):
        try:
            ser.write(TIME_HEADER + str(int(time.time())))
        except:
            print("error writing time")
    else:
        print(newLine)
        #parse sensor data

#ser.open()
while True:
    newLine = ser.readline()
    if newLine:
        reactToNewLine(newLine)

#str(int(time.time()+TimeZone))
