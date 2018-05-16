import serial
from time import sleep

ser = serial.Serial ("/dev/ttyAMA0", 9600)
while True:
    received_data = ser.readline()              #read serial port
    sleep(0.03)
    print (received_data)                   #print received data

