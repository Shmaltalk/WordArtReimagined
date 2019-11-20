# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
from random import randrange
GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout


# Set up pin 11 for PWM
GPIO.setup(11,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
p1 = GPIO.PWM(11, 50)     # Sets up pin 11 as a PWM pin

#GPIO.setup(13, GPIO.OUT)
#p2 = GPIO.PWM(13, 50)

p1.start(0)               # Starts running PWM on the pin and sets it to 0
#p2.start(0)


def move_servo(servo, degree):
	p = 0
	if (servo == 1):
		p = p1
	elif (servo == 2):
		p = p2
	else:
		return
	dc = (degree/180.0)*10 + 2.5
	# Move the servo back and forth
	p.ChangeDutyCycle(dc)     # 2.5 os 0deg, 7.5 is 90deg, 12.5 is 180deg
	sleep(1)                  # Wait 1 second

for i in range(10):
        move_servo(1, randrange(181))

# Clean up everything
p1.stop()                 # At the end of the program, stop the PWM
p2.stop()
GPIO.cleanup()           # Resets the GPIO pins back to defaults
