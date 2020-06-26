import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Name(tk.Tk):
    def __init__(self):
        super().__init__()

    def input_expression(self):
        # self.input_exp = tk.StringVar()
        self.input_exp = tk.Entry(self, font='Arial 20', width=25, bg='black', foreground='white')
        self.input_exp.grid(column=0, row=0, sticky='w')

    def num7(self):
        self.input_exp.insert('end', 7)

    def num8(self):
        self.input_exp.insert('end', 8)

    def num9(self):
        self.input_exp.insert('end', 9)

    def multiply(self):
        self.input_exp.insert('end', '*')

    def divide(self):
        self.input_exp.insert('end', '/')

    def num4(self):
        self.input_exp.insert('end', 4)

    def num5(self):
        self.input_exp.insert('end', 5)

    def num6(self):
        self.input_exp.insert('end', 6)

    def substract(self):
        self.input_exp.insert('end', '-')

    def addition(self):
        self.input_exp.insert('end', '+')

    def num1(self):
        self.input_exp.insert('end', 1)
    
    def num2(self):
        self.input_exp.insert('end', 2)

    def num3(self):
        self.input_exp.insert('end', 3)

    def evaluate(self):
        try:
            self.output = str(float(eval(self.input_exp.get())))
            self.input_exp.delete(0, tk.END)
            self.input_exp.insert(0, self.output)
        except SyntaxError:
            tk.messagebox.showerror('Error','Your imput is wrong')
        except :
            tk.messagebox.showerror('Error','Something went wrong !')

    def num0(self):
        self.input_exp.insert('end', 0)

    def decimal(self):
        self.input_exp.insert('end', '.')
        
    def clear(self):
        self.input_exp.delete(len(self.input_exp.get())-1)

    def clear_all(self):
        self.input_exp.delete(0, tk.END)

    def keys(self):
        self.keys_frame = tk.Frame(self)
        self.keys_frame.grid(column=0, row=1)

        self.num7 = tk.Button(self.keys_frame, text='7', padx=20, pady=15, font='arial 18', command=self.num7)
        self.num7.grid(column=0, row=1, sticky='w')

        self.num8 = tk.Button(self.keys_frame, text='8', padx=20, pady=15, font='arial 18', command=self.num8)
        self.num8.grid(column=1, row=1, sticky='w')

        self.num9 = tk.Button(self.keys_frame, text='9', padx=20, pady=15, font='arial 18', command=self.num9)
        self.num9.grid(column=2, row=1, sticky='w')

        self.multiply = tk.Button(self.keys_frame, text='*', padx=20, pady=15, font='arial 18', command=self.multiply)
        self.multiply.grid(column=3, row=1, sticky='w')

        self.divide = tk.Button(self.keys_frame, text='/', padx=20, pady=15, font='arial 18', command=self.divide)
        self.divide.grid(column=4, row=1, sticky='w')



        self.num4 = tk.Button(self.keys_frame, text='4', padx=20, pady=15, font='arial 18', command=self.num4)
        self.num4.grid(column=0, row=2, sticky='w')

        self.num5 = tk.Button(self.keys_frame, text='5', padx=20, pady=15, font='arial 18', command=self.num5)
        self.num5.grid(column=1, row=2, sticky='w')

        self.num6 = tk.Button(self.keys_frame, text='6', padx=20, pady=15, font='arial 18', command=self.num6)
        self.num6.grid(column=2, row=2, sticky='w')

        self.substract = tk.Button(self.keys_frame, text='-', padx=20, pady=15, font='arial 18', command=self.substract)
        self.substract.grid(column=3, row=2, sticky='w')

        self.addition = tk.Button(self.keys_frame, text='+', padx=16, pady=15, font='arial 18', command=self.addition)
        self.addition.grid(column=4, row=2, sticky='w')



        self.num1 = tk.Button(self.keys_frame, text='1', padx=20, pady=15, font='arial 18', command=self.num1)
        self.num1.grid(column=0, row=3, sticky='w')

        self.num2 = tk.Button(self.keys_frame, text='2', padx=20, pady=15, font='arial 18', command=self.num2)
        self.num2.grid(column=1, row=3, sticky='w')

        self.num3 = tk.Button(self.keys_frame, text='3', padx=20, pady=15, font='arial 18', command=self.num3)
        self.num3.grid(column=2, row=3, sticky='w')

        self.evaluate = tk.Button(self.keys_frame, text='=', padx=50, pady=15, font='arial 18', command=self.evaluate)
        self.evaluate.grid(column=3, columnspan=2, row=3, sticky='w')



        self.num0 = tk.Button(self.keys_frame, text='0', padx=20, pady=15, font='arial 18', command=self.num0)
        self.num0.grid(column=0, row=4, sticky='w')

        self.decimal = tk.Button(self.keys_frame, text='.', padx=22, pady=15, font='arial 18', command=self.decimal)
        self.decimal.grid(column=1, row=4, sticky='w')

        self.clear = tk.Button(self.keys_frame, text='C', padx=18, pady=15, font='arial 18', command=self.clear)
        self.clear.grid(column=2, row=4, sticky='w')

        self.clear_all = tk.Button(self.keys_frame, text='CA', padx=40, pady=15, font='arial 18', command=self.clear_all)
        self.clear_all.grid(column=3, columnspan=2, row=4, sticky='w')


n = Name()
n.input_expression()
n.keys()

n.mainloop()
