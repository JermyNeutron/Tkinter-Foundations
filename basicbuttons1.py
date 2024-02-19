import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Everything About Buttons')
window.geometry('800x500')

# functions
def button_func():
    print('a basic button')



# buttons
button_string = tk.StringVar(value='basic button')
button = ttk.Button(window, text='button', command= lambda: print('a more basic button'), textvariable=button_string)
button.pack()

# check button
check_var = tk.StringVar()
buttoncheck = ttk.Checkbutton(window, text='my first check', command= lambda: print(check_var.get()), variable=check_var)
buttoncheck.pack()

# radio button
radio1_var = tk.StringVar()
radio2_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, text= 'radiobutton ', value= 'hello', variable= radio1_var, command=lambda: print(radio1_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, text= 'radiobutton ', value= 2, variable= radio2_var, command=lambda: print(radio2_var.get()))
radio2.pack()

# exercise function
def radio_func():
    print(exercise_check_var.get())
    exercise_check_var.set(0)

# exercise
exercise_radio_var = tk.StringVar()
exercise_label = ttk.Label(window, text='Exercise')
exercise_label.pack(pady=10)
radio3 = ttk.Radiobutton(window, text='A', value='A', variable=exercise_radio_var, command=radio_func)
radio4 = ttk.Radiobutton(window, text='B', value= 'B', variable=exercise_radio_var, command=radio_func)
radio3.pack()
radio4.pack()

exercise_check_var = tk.BooleanVar()
check2 = ttk.Checkbutton(window, text='exercise checker', variable=exercise_check_var, command=lambda:print(exercise_radio_var.get()))
check2.pack()

# run
window.mainloop()