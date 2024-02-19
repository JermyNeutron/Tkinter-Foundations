# Combo and Spin Box
# combo is a drop-down box
# spin box is an increment field

import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('Combo & Spin Box')
window.geometry('500x500')

# Combobox
items = ('ice cream', 'pizza', 'broccoli')
food_string = tk.StringVar(value= '(select item)')
combo = ttk.Combobox(window, textvariable=food_string)
combo.configure(values= items) # or combo['values'] = items
combo.pack()

# events
combo.bind('<<ComboboxSelected>>', lambda event: print(f'{food_string.get()} selected')) #executes function whenever an item in combobox is selected
combo.bind('<<ComboboxSelected>>', lambda event: label.configure(text= f'Selected value: {food_string.get()}')) #executes function whenever an item in combobox is selected

# label
label = ttk.Label(window, text= 'a label')
label.pack()



# spin box
spinbox_int = tk.IntVar(value=12)
spinbox = ttk.Spinbox(window,
                      from_=3,
                      to=20,
                      increment=3,
                      command= lambda: print('a button was pressed'),
                      textvariable= spinbox_int)
spinbox.bind('<<Increment>>', lambda event: print('up was pressed'))
spinbox.bind('<<Decrement>>', lambda event: print('down was pressed'))
# spinbox.configure(values=(1,2,3,4,5))
spinbox.pack()

# exercise
# create a spinbox that contains the letters A B C D E
#  print the value whenever the value is decreased

ex_label = ttk.Label(window, text='Exercise')
ex_label.pack(pady=20)
ex_spin_values = ('A', 'B', 'C', 'D', 'E')
ex_spin_def = tk.StringVar(value= 'select a value')
ex_spin = ttk.Spinbox(window,
                      values= ex_spin_values,
                      textvariable= ex_spin_def)
ex_spin.bind('<<Decrement>>', lambda event: print(f'{ex_spin_def.get()} was selected'))
ex_spin.pack()

# run
window.mainloop()