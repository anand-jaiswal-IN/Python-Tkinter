from datetime import datetime
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

class Notepad(tk.Tk):

    file_opened = None

    def __init__(self):
        super().__init__()
        self.geometry("800x300")
        self.title('Untitled - Notepad')

    def newFile(self):
        self.textarea.delete(1.0, tk.END)
        self.title('Untitled - Notepad')
        Notepad.file_opened = None
        
    def openFile(self):
        try:
            Notepad.file_opened = filedialog.askopenfile(title='Open text file', initialdir='/', filetypes = (("Txt files", "*.txt"), ("All files", "*.*"))).name

            self.textarea.delete(1.0, tk.END)

            with open(Notepad.file_opened, 'r') as file:
                self.textarea.insert(1.0, file.read())
            self.title(Notepad.file_opened.split('/')[-1])
            
        except AttributeError:
            messagebox.showerror('File Not Found', 'You have not selected any file')
        except UnicodeDecodeError:
            messagebox.showerror('File not correct', 'You have selected wrong file format')
    
    def saveFile(self):
        try:
            with open(Notepad.file_opened, 'w') as file:
                self.text_typed = self.textarea.get(1.0, tk.END)
                self.textarea.delete(1.0, tk.END)
                file.write(self.text_typed)
                self.textarea.insert(1.0, self.text_typed)

        except TypeError:
            self.saveasFile()

    def saveasFile(self):
        try:
            Notepad.file_opened = filedialog.asksaveasfile(title='Save File', initialdir='/', defaultextension='.txt').name

            self.title(Notepad.file_opened.split('/')[-1])

            with open(Notepad.file_opened, 'w') as file:
                file.write(self.textarea.get(1.0, tk.END))
                
        except AttributeError:
            messagebox.showerror('File not defined', 'You have not save the file')

    def undoText(self):
        try:
            self.textarea.edit_undo()
        except:
            return

    def redoText(self):
        try:
            self.textarea.edit_redo()
        except:
            return

    def cutText(self):
        self.copyText()
        self.selDelete()

    def copyText(self):
        self.textarea.clipboard_clear()
        self.textarea.clipboard_append(self.textarea.selection_get())

    def pasteText(self):
        self.textarea.insert(tk.INSERT, self.textarea.clipboard_get())

    def selDelete(self):
        self.textarea.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def selAll(self):
        self.textarea.tag_add(tk.SEL, "1.0", tk.END)
        self.textarea.mark_set(tk.INSERT, "1.0")
        self.textarea.see(tk.INSERT)
        return 'break'

    def insertDateTime(self):
        time_date = datetime.now().strftime("%H:%M %d-%m-%Y")
        self.textarea.insert(tk.INSERT, time_date)

    def wordWrap(self):
        if self.wordWrap_checkbutton.get()==1:
            self.textarea.config(wrap='word')
        else:
            self.textarea.config(wrap='none')
    
    def aboutNotepad(self):
        self.aboutNotepadWindow = tk.Toplevel()
        self.aboutNotepadWindow.title('About Notepad')
        path = 'anand.jpg'
        self.anand_img = ImageTk.PhotoImage(Image.open(path))
        tk.Label(self.aboutNotepadWindow, image=self.anand_img).pack()
        tk.Label(self.aboutNotepadWindow, text='DEVELOPED BY ANAND JAISWAL', font='Arial 30').pack()

    def top_menubar(self):
        self.menubar = tk.Menu(self) # toplevel_menubar
        self.config(menu=self.menubar)

        self.file_menu = tk.Menu(self.menubar, tearoff=0) # filemenu
        self.edit_menu = tk.Menu(self.menubar, tearoff=0) # editmenu
        self.format_menu = tk.Menu(self.menubar, tearoff=0) # formatmenu
        self.help_menu = tk.Menu(self.menubar, tearoff=0) # aboutmenu

        # submenu in filemenu
        self.file_menu.add_command(label='New', command=self.newFile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Open', command=self.openFile)
        self.file_menu.add_command(label='Save', command=self.saveFile)
        self.file_menu.add_command(label='Save As', command=self.saveasFile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.destroy)

        # submenu in editmenu
        self.edit_menu.add_command(label='Undo', command=self.undoText)
        self.edit_menu.add_command(label='Redo', command=self.redoText)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Cut', command=self.cutText)
        self.edit_menu.add_command(label='Copy', command=self.copyText)
        self.edit_menu.add_command(label='Paste', command=self.pasteText)
        self.edit_menu.add_command(label='Delete', command=self.selDelete)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Select All', command=self.selAll)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Time/Date', command=self.insertDateTime)
        

        # submenu of formatmenu
        self.wordWrap_checkbutton = tk.IntVar()
        self.format_menu.add_checkbutton(label='Word Wrap', command=self.wordWrap, variable=self.wordWrap_checkbutton)

        # submenu of aboutmenu
        self.help_menu.add_command(label='About Notepad', command=self.aboutNotepad)


        self.menubar.add_cascade(label='File', menu=self.file_menu) # adding more menus
        self.menubar.add_cascade(label='Edit', menu=self.edit_menu) # adding more menus
        self.menubar.add_cascade(label='Format', menu=self.format_menu) # adding more menus
        self.menubar.add_cascade(label='Help', menu=self.help_menu) # adding more menus

    def textarea_for_type(self):
        self.scrollbarY = tk.Scrollbar(self) # scrollbar for textarea
        self.scrollbarY.pack(side=tk.RIGHT, fill=tk.Y) # packing schrollbar

        self.scrollbarX = tk.Scrollbar(self, orient=tk.HORIZONTAL) # scrollbar for textarea
        self.scrollbarX.pack(side=tk.BOTTOM, fill=tk.X) # packing schrollbar

        self.textarea = tk.Text(self, font='Arial 20', yscrollcommand=self.scrollbarY.set, xscrollcommand=self.scrollbarX.set, undo=True, wrap='char') # textarea in notepad
        self.textarea.focus_set()
        self.textarea.pack(fill=tk.BOTH)

        self.scrollbarY.config(command=self.textarea.yview)
        self.scrollbarX.config(command=self.textarea.xview)
        


n = Notepad()
n.top_menubar()
n.textarea_for_type()



n.mainloop()