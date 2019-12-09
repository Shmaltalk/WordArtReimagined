from math import atan, asin, degrees, sqrt
import serial
from time import sleep
import math


def get_angles(x, y):
    r = sqrt(x*x + y*y)
    angle2 = 2 * degrees(asin(r/14))
    angle1 = degrees(atan(y/x)) + (90 - angle2/2)
    return (angle1, angle2)

def servo_setup():
    ser = serial.Serial('/dev/ttyACM0', 9600)

    global last_x
    last_x = -5.5
    global last_y
    last_y = 2.75
    return ser



def move_servos(ser, x, y):
    global last_x
    global last_y
    x = (x - 300) / 50
    y = y / 50 + 1

    distance = math.sqrt((x - last_x) ** 2 + (y - last_y) ** 2)
    prog = 0
    while prog < distance:
        frac = prog / distance
        xvect = x - last_x
        yvect = y - last_y
        curr_x = last_x + xvect * frac
        curr_y = last_y + yvect * frac

        #print(f'{x}, {y}')
        servo1, servo2 = get_angles(curr_x, curr_y)
        if servo1 > 90:
            servo1 = servo1 - 180

        ser.write(f'{int((85 - servo1) / 180 * 2100 + 450)},{int((180 - servo2) / 180 * 1450 + 605)};'.encode('utf-8'))
        #print(f'{int(servo1)},{int(servo2)};')

        sleep(.02)
        prog += .03

    #print(f'{x}, {y}')
    servo1, servo2 = get_angles(x, y)
    if servo1 > 90:
        servo1 = servo1 - 180

    ser.write(f'{int((85 - servo1) / 180 * 2100 + 450)},{int((180 - servo2) / 180 * 1450 + 605)};'.encode('utf-8'))
    #print(f'{int(servo1)},{int(servo2)};')

    #sleep(.25)                  # Wait 1 second
    last_x = x
    last_y = y
