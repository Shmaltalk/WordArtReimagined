import tkinter as tk
import aggdraw

from sentinalysis import get_sentinalysis
from line_patterns import pattern2num, num2pattern
from points import draw_pattern

def draw():
    sentinalysis_values = get_sentinalysis()
    pattern_list = []
    for tup in sentinalysis_values:
        pattern_list.append(get_pattern(tup))

    root = tk.Tk() # temp

    size = 800, 500 # temp
    draw = aggdraw.Dib("RGB", size) # temp

    i = 100
    i_dir = 1
    j = 200
    for pat, mult in pattern_list:
        if i >= 500 or i<=100: # at horizontal edges
            i_dir *= -1 # switch drawing directions
            j += 20 # increment y val
        draw_pattern(pat, mult)
        i += 10 * i_dir * mult
        draw.line(xy, aggdraw.Pen("red", 1)) # temp

    frame = tk.Frame(root, width=size[0], height=size[1], bg="") # temp
    frame.bind("<Expose>", lambda e: draw.expose(hwnd=e.widget.winfo_id())) # temp
    frame.pack() # temp

    tk.mainloop() # temp

def draw_pattern(patternNum, mult):
    pattern = num2pattern[patternNum]
    xy = []
    for p in pattern:
        xy.append(p[0] * i_dir * mult + i)
        xy.append(p[1] * i_dir * mult + j)
    draw.line(xy, aggdraw.Pen("red", 1))

def get_pattern(tup):
    pos = tup[0]
    neg = tup[1]
    neu = tup[2]

    if (pos > neg):
        if (neg >= neu):
            return (pattern2num("loop"), 6+((pos-neg)*5)) # pos > neg >= neu
        elif (pos >= neu): # pos >= neu > neg
            return (pattern2num("double_loop"), 6+((pos-neu)*5))
        else: # neu > pos > neg
            return (pattern2num("flat"), 6+((neu-pos)*5))
    else:
        if (pos >= neu): # neg >= pos >= neu
            return (pattern2num("madisons_stupid_line"), 6+((neg-pos)*5))
        elif (neg >= neu): # neg >= neu > pos
            return (pattern2num["arc"], 6+((neg-neu)*5))
        else: # neu > neg >= pos
            return (pattern2num["wavy_line"], 6+((neu-neg)*5))

draw()