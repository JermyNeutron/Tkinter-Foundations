import tkinter as tk
from tkinter import ttk

# functions
def button_func():
    print(string_var.get())
    string_var.set('')
# window
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('800x500')

# tkinter variables
# string_var = tk.StringVar()
# int_var = tk.IntVar()
# double_var = tk.DoubleVar()
# boolean_var = tk.BooleanVar()
string_var = tk.StringVar(value='hello')


# widgets
label = ttk.Label(master=window, text='label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

# button
button = ttk.Button(master=window, text='button', command=button_func)
button.pack()

string_var2 = tk.StringVar(value='test')

# exercise
entry2 = ttk.Entry(master=window, textvariable=string_var2)
entry3 = ttk.Entry(master=window, textvariable=string_var2)
entry2.pack()
entry3.pack()

label2 = ttk.Label(master=window, textvariable=string_var2)
label2.pack()

# run
window.mainloop()