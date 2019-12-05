from math import atan, asin, degrees, sqrt

import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program

def servo_setup():

    GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout

    GPIO.setup(11,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
    p1 = GPIO.PWM(11, 50)     # Sets up pin 11 as a PWM pin

    GPIO.setup(13,GPIO.OUT)  # Sets up pin 13 to an output (instead of an input)
    p1 = GPIO.PWM(13, 50)     # Sets up pin 13 as a PWM pin

    p1.start(0)               # Starts running PWM on the pin and sets it to 0
    p2.start(0)               # Starts running PWM on the pin and sets it to 0
    return (p1, p2)

def get_angles(x, y):
    r = sqrt(x*x + y*y)
    angle2 = 2 * degrees(asin(r/2)/7)
    angle1 = atan(y/x) + (90 - angle2/2)
    return (angle1, angle2)


def move_servos(p1, p2, x, y):
    servo1, servo2 = get_angles(x, y)
    
    dc1 = (servo1/18.0) + 2.5
    dc2 = (servo2/18.0) + 2.5

    # Move the servo back and forth
    p1.ChangeDutyCycle(dc1)     # 2.5 os 0deg, 7.5 is 90deg, 12.5 is 180deg
    p2.ChangeDutyCycle(dc2)     # 2.5 os 0deg, 7.5 is 90deg, 12.5 is 180deg

    print(dc1, dc2)
	
    sleep(.25)                  # Wait 1 second