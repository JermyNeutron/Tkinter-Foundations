import tkinter as tk
import tkinter as ttk

# functions
def button_func():
    print('a button was pressed')

def button2_func():
    print('hello')

# window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master=window, text='this is a text')
label.pack()

# tk widgets
text_window = tk.Text(master=window)
text_window.pack()

# ttk entry, single line entry widget
entry = ttk.Entry(master=window)
entry.pack()

label2 = ttk.Label(master=window, text="my label")
label2.pack()

# ttk button
button = ttk.Button(master=window, text='button', command=button_func)
button.pack()

# button2
# button2 = ttk.Button(master=window, text="exercise button", command=button2_func)
button2 = ttk.Button(master=window, text="exercise button", command= lambda: print('hello'))
button2.pack()

# run
window.mainloop()