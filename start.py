#This is where the program starts
import db
import serial

ser = serial.Serial('/dev/cu.usbmodem1411', 115200)
count = 0
while True:
    putIntoList(ser.readline())
    count += 1
    if count > 1000:
        startMonitoringVideoFeed()
        break
        
while True:
    putIntoList(ser.readline())