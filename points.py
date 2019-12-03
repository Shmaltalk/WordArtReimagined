
import tkinter as tk
import aggdraw
from line_patterns import num2pattern

root = tk.Tk()

# SERVO 1 goes from 2.5 - 12

"""arc = wavy_line
print('[')
for i in range(len(arc)):
    arc[i] = ((arc[i][0]-6.28) * 10/(8.29-6.28), (arc[i][1] - 1) * 10/(8.29-6.28))
    print(f'({arc[i][0]:.2f}, {arc[i][1]:.2f}),')
print(']')
"""


def draw_pattern(patternNum, mult):

    for j in range(200, 400, 10): # y min/max/step
        i = 100
        while i < 500:
            pattern = num2pattern[patternNum]
            xy = []
            for p in pattern:
                xy.append(p[0] * abs(mult) + i)
                xy.append(p[1] * mult + j)
            i += 10 * abs(mult)

            draw.line(xy, aggdraw.Pen("red", 1))


"""frame = tk.Frame(root, width=size[0], height=size[1], bg="")
frame.bind("<Expose>", lambda e: draw.expose(hwnd=e.widget.winfo_id()))
frame.pack()

tk.mainloop()
"""
