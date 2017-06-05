from time import sleep
import sys
import serial

def init(port_name= '/dev/ttyUSB1'):
    global ser
    ser = serial.Serial(portname, 9600) # Establish the connection on a specific port

def send_char(char):
    ser.write(char)
    sleep(.1)

def send_command(string):
    for s in string:
        send_char(s)

if __name__ == '__main__':
    init()
    sleep(2)
    send_command(sys.argv[1])



