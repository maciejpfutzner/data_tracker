from time import sleep
import sys
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600) # Establish the connection on a specific port

def send_char(char):
    ser.write(char)
    sleep(.1)

def send_command(string):
    for s in string:
        send_char(s)

if __name__ == '__main__':
    send_command(sys.argv)



