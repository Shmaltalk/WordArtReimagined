import tkinter as tk
import random
import RPi.GPIO as GPIO
import time

from sentinalysis import get_sentinalysis
from line_patterns import pattern2num, num2pattern
from points import draw_pattern
from servo_control_arduino import servo_setup, move_servos

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def draw_control():
    serial = servo_setup()
    i = 100
    j = 100
    i_dir = 1
    
    move_servos(serial, 100, 100)
    check_button_push(0)
    sentinalysis_values = get_sentinalysis()

    while (True):
        i, j, i_dir = draw(serial, sentinalysis_values, i, j, i_dir)

        if (not check_button_push(15)):
            move_servos(serial, 100, 100)
            i = 100
            j = 100
            i_dir = 1
            check_button_push(0)
        
        sentinalysis_values = []
        sentinalysis_values = get_sentinalysis()

    serial.close()

def check_button_push(wait_time):
    if (wait_time>0):
        start_time = time.time()
        while (time.time()-start_time < wait_time):
            if GPIO.input(10) == GPIO.LOW:
                return True
        return False
    else:
        while (True):
            if GPIO.input(10) == GPIO.LOW:
                return True
    

def draw(serial, sentinalysis_values, i, j, i_dir):
    # move_servos(serial, 100, 100)
    print(sentinalysis_values)
    pattern_list = []

    for tup in sentinalysis_values:
        curr_pattern = get_pattern(tup)
        pattern_list.append(curr_pattern)

    print(pattern_list)

    for pat, mult in pattern_list:
        i_temp = i + (10 * i_dir * mult) # make sure we're not about to overshoot
        if i_temp >= 500 or i_temp<=100: # at horizontal edges
            i_dir *= -1 # switch drawing directions
            j += 40 # increment y val
        xy = draw_pattern(pat, mult, i_dir, i, j)
        i += 10 * i_dir * mult
        for x, y in xy:
            move_servos(serial, x, y)
    return (i, j, i_dir)

def draw_pattern(patternNum, mult, i_dir, i, j):
    pattern = num2pattern[patternNum]
    xy = []
    for p in pattern:
        xy.append((p[0] * i_dir * mult + i, p[1] * mult + j))
    return xy

def get_pattern(tup):
    pos = tup[0]
    neg = tup[1]
    neu = tup[2]

    #return (random.randint(0, 5), random.random()*2 + 4)
    size_ratio = 7
    if (neu == 1):
        return (pattern2num["flat"], 3)
    elif (neu > .75):
        return (pattern2num["wavy_line"], (neu*size_ratio))
    elif (pos < .25):
        if (neg < .25):
            return (pattern2num["arc"], 3)
        else:
            if (neu>neg):
                return (pattern2num["madisons_stupid_line_updwn"], (neg*size_ratio))
            else:
                return (pattern2num["madisons_stupid_line"], (neg*size_ratio))
    else:
        if (neg < .25):
            if (neu>pos):
                return (pattern2num["double_loop_updwn"], (pos*size_ratio))
            else:
                return (pattern2num["double_loop"], (pos*size_ratio))
        else:
            return (pattern2num["loop"], (max(pos, neg)*size_ratio))



draw_control()


