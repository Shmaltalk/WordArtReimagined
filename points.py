import math
import tkinter as tk
import aggdraw
import random
from line_patterns import double_loop, arc, loop, madisons_stupid_line, flat, wavy_line

root = tk.Tk()

# SERVO 1 goes from 2.5 - 12



choices = [double_loop, arc, loop, madisons_stupid_line, flat, wavy_line]

"""arc = wavy_line
print('[')
for i in range(len(arc)):
    arc[i] = ((arc[i][0]-6.28) * 10/(8.29-6.28), (arc[i][1] - 1) * 10/(8.29-6.28))
    print(f'({arc[i][0]:.2f}, {arc[i][1]:.2f}),')
print(']')
"""

size = 800, 500

draw = aggdraw.Dib("RGB", size)


for j in range(200, 400, 10):
    i = 100
    while i < 500:
        choice = choices[random.randint(0, len(choices) - 1)]
        xy = []
        mult = (random.random() - 0.5) * 7
        mult += abs(mult) / mult
        for p in choice:
            xy.append(p[0] * abs(mult) + i)
            xy.append(p[1] * mult + j)
        i += 10 * abs(mult)

        draw.line(xy, aggdraw.Pen("red", 1))


frame = tk.Frame(root, width=size[0], height=size[1], bg="")
frame.bind("<Expose>", lambda e: draw.expose(hwnd=e.widget.winfo_id()))
frame.pack()

tk.mainloop()
