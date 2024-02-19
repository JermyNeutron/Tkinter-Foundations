# Canvas

import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('500x500')
window.title('Canvas')

# # canvas
# canvas = tk.Canvas(window, bg='white')
# canvas.pack()

# canvas.create_rectangle((50,20,100,200), fill= 'red', width=10, dash=(2,1,1), outline='green')
# canvas.create_line(50, 50, 200, 200)
# canvas.create_oval((100,9,300,100), fill='magenta', width=0)
# # canvas.create_polygon((0,0), (100,200), (300,50), width=0, fill='yellow')
# canvas.create_arc((100,9,300,100), fill='yellow', start = 45, extent= 140, style = tk.CHORD, outline = 'red', width = 10)

# # draw text
# canvas.create_text((100,100), text='this is some text', width=40)

# canvas.create_window((100,100), window=ttk.Button(window, text='this is text in a canvas'))

# exercise
# use event binding to create a basic paint app
ex_label = ttk.Label(window, text='Exercise')
ex_label.pack(pady=20 )

# canvas
canvas = tk.Canvas(window, bg='white')
canvas.pack()

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size/2,
                       y - brush_size/2,
                       x + brush_size/2,
                       y + brush_size/2))

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4

    brush_size = max(0, min(brush_size, 50))
    print(event)

brush_size = 4
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)

# run
window.mainloop()