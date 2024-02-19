import tkinter as tk
from tkinter import ttk

def button_func():
    # print(entry.get())
    # entry_text = entry.get()
    # update label
    # label.configure(text= 'some other text')
    label['text'] = entry.get()
    print(label['text'])
    entry.configure(state= 'disabled')

def button2_func():
    label['text'] = 'some text'
    entry.configure(state= 'enabled')

# window
window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('800x500')

# widgets
label = ttk.Label(master=window, text='some text')
label.pack()

# entry
entry = ttk.Entry(master=window)
entry.pack()

# button
button = ttk.Button(master=window, text='the button', command= button_func)
button.pack()

# button2
button2 = ttk.Button(master=window, text='reset', command=button2_func)
button2.pack()

# run
window.mainloop()