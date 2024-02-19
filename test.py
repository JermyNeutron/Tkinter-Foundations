import tkinter as tk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename='darkly')
window.title('SLP Checker')
window.minsize(500,250)

# label
label_main = ttk.Label(master=window, text='Super Lotto Plus', font="Calibri 24")
label_main.pack()

#
entry = tk.Entry()
entry.pack()

# key bind events
window.bind('<Return>', function)

window.mainloop()