import math
import tkinter as tk
import aggdraw
import random

root = tk.Tk()

loop = [
(0.00, 0.00),
(1.23, -0.25),
(2.46, -0.59),
(4.14, -1.33),
(5.22, -2.02),
(6.35, -2.91),
(7.44, -4.33),
(8.13, -6.60),
(7.44, -9.21),
(6.31, -10.05),
(5.27, -10.20),
(4.19, -9.70),
(3.30, -8.67),
(2.71, -6.55),
(3.30, -4.19),
(4.14, -2.96),
(5.22, -2.02),
(7.54, -0.79),
(8.77, -0.44),
(10.00, 0.00),
]

sharp = [
(0.00, 0.00),
(5.00, -10.00),
(10.00, 0.00),
]

flat = [
(0.00, 0.00),
(10.00, 0.00),
]

arc = [
(0.00, 0.00),
(-0.24, -2.20),
(-0.31, -4.41),
(0.04, -6.50),
(1.61, -8.35),
(4.45, -9.02),
(7.17, -8.54),
(9.09, -7.01),
(9.69, -4.96),
(9.84, -2.68),
(10.00, 0.00),
]

madisons_stupid_line = [
(0, 0),
(2, 5),
(5, 0),
(8, -5),
(10, 0),
]

choices = [loop, arc, flat]

"""
print('[')
for i in range(len(arc)):
    arc[i] = ((arc[i][0]-2.93) * 10/(5.47-2.93), (arc[i][1] - 6.9) * 10/(5.47-2.93))
    print(f'({arc[i][0]:.2f}, {arc[i][1]:.2f}),')
print(']')
"""

size = 800, 500

draw = aggdraw.Dib("RGB", size)


for j in range(200, 400, 40):
    i = 100
    while i < 500:
        choice = choices[random.randint(0, len(choices) - 1)]
        xy = []
        mult = (random.random() - 0.5) * 10
        mult += abs(mult) / mult
        for p in choice:
            xy.append(p[0] * abs(mult) + i)
            xy.append(p[1] * mult + j)
        i += 10 * abs(mult)

        draw.line(xy, aggdraw.Pen("red"))


frame = tk.Frame(root, width=size[0], height=size[1], bg="")
frame.bind("<Expose>", lambda e: draw.expose(hwnd=e.widget.winfo_id()))
frame.pack()

tk.mainloop()
