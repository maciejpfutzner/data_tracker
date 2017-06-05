from time import sleep
import sys
import glob
import serial

def find_port():
    if sys.platform == 'darwin':
        ports = glob.glob('/dev/tty.w*')
        return ports[0]
    elif 'linux' in sys.platform:
        ports = glob.glob('/dev/ttyUSB*')
        return ports[0]
    else:
        print "Don't know about Windows or other systems"
        return None

#def init(port_name= '/dev/ttyUSB1'):
def init(port_name=None):
    if not port_name:
        port_name = find_port()
    global ser
    ser = serial.Serial(port_name, 9600) # Establish the connection on a specific port
    sleep(2) # sleep to let arduino restart

def send_char(char):
    ser.write(char)
    sleep(.01)

def send_command(string):
    for s in string:
        send_char(s)

if __name__ == '__main__':
    init()
    send_command(sys.argv[1])



