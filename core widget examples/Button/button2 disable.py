# How to disable a button for debug etc so as not to confuse testers

from tkinter import *

master = Tk()

b = Button(master, text='Help!', state=DISABLED)
b.pack()

mainloop()