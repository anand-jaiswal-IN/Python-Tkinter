import tkinter as tk
from tkinter import ttk
win = tk.Tk(className='Anand GUI')

# label
ttk.Label(win, text='Enter your name : ').grid(column=0, row=0, sticky=tk.W)
ttk.Label(win, text='Enter your age : ').grid(column=0, row=1, sticky=tk.W)
ttk.Label(win, text='Select your gender : ').grid(column=0, row=2, sticky=tk.W)

# variable
name = tk.StringVar()
age = tk.IntVar()
gender = tk.StringVar()

# Entry box
name_entry = ttk.Entry(win, width=15, textvariable=name)
name_entry.focus()
name_entry.grid(column=1, row=0)

age_entry = ttk.Entry(win, width=15, textvariable=age)
age_entry.delete(0, 'end')
age_entry.grid(column=1, row=1)

# radiobox
male_radio = ttk.Radiobutton(win, text='Male', value='Male', variable=gender)
male_radio.grid(column=1, row=2, sticky=tk.W)

female_radio = ttk.Radiobutton(win, text='Female', value='Female', variable=gender)
female_radio.grid(column=2, row=2, sticky=tk.W)

# button command
def submit_data():
    print(name.get(), age.get(), gender.get())

def reset_data():
    name_entry.delete(0, 'end')
    age_entry.delete(0, 'end')
    
#button
ttk.Button(win, text='Submit', command=submit_data).grid(column=0, row=4, sticky=tk.W)
ttk.Button(win, text='Reset', command=reset_data).grid(column=1, row=4, sticky=tk.W)







win.mainloop()