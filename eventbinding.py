# event binding
import tkinter as tk
from tkinter import ttk

def exit_application():
    window.quit()
    print('application was closed.\ngoodbye')

def get_pos(event):
    print(f'x: x{event.x} y: {event.y}')

# window
window = tk.Tk()
window.title('Event Binding')
window.geometry('500x500')

# text
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window,)
entry.pack()

btn = ttk.Button(window, text='a button', command=exit_application)
btn.pack()

# events
# window.bind('<Control-KeyPress-s>', lambda event: print(event))
# text.bind('<Motion>', get_pos)

# entry.bind('<FocusIn>', lambda event: print('entry field was selected'))

# exercise
# print 'mousewheel' when the user holds down shift and uses the mousewheel while text is selected
text.bind('<Shift-MouseWheel>', lambda event: print('Mousehweel'))

# run
window.mainloop()