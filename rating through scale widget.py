import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tmsg


win = tk.Tk(className='Your desired window name')
def submit_rating():
    tmsg.showinfo(f'Rating', 'Thankyou for your attention, Keep join us !\n\n Your rating is {}'.format(rating.get()))

rating = tk.Scale(win, from_= 1, to=5, label='Please rate our product !!!', length=300, orient='horizontal', tickinterval=1, showvalue=0)
rating.pack()

tk.Button(win, text='Submit', command=submit_rating).pack()

win.mainloop()