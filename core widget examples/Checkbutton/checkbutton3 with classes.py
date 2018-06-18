# If code is already placed in a class, as should be done, it's cleaner to store the variable in an attribute, and use a bound method as callback
from tkinter import *
class App:

    def __init__(self, master):
        self.var = IntVar()
        c = Checkbutton(
            master, text='Enable Tab',
            variable=self.var,
            command=self.cb)
        c.pack()

    def cb(self): # the original code had, event) but maybe that's legacy python 2 code?  Look into it later
        print('variable is', self.var.get())

master = Tk()

app = App(master)
mainloop()