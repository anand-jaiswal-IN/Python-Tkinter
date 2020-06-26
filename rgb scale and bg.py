import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
class Name(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x600')

    def _from_rgb(self, rgb):
        return "#%02x%02x%02x" % rgb
            

    def chg_bg(self):
        self.config(bg=self._from_rgb((self.r_value.get(), self.g_value.get(), self.b_value.get())))
        

    def color(self):
        self.rgb_range = tk.Frame(self)
        self.rgb_range.pack()

        self.r_value = tk.Scale(self.rgb_range, to=0, from_=255, length=500, label='R_value')
        self.r_value.grid(column=0, row=0)

        self.g_value = tk.Scale(self.rgb_range, to=0, from_=255, length=500, label='G_value')
        self.g_value.grid(column=1, row=0)

        self.b_value = tk.Scale(self.rgb_range, to=0, from_=255, length=500, label='B_value')
        self.b_value.grid(column=2, row=0)

        tk.Button(self.rgb_range, text='Submit', command=self.chg_bg, padx=10, pady=10).grid(row=1, column=1)
            


n = Name()
n.color()
n.mainloop()