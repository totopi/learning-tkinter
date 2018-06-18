# You can also bind the entry widget to a StringVar instance, and set or get the entry text from that variable:
from tkinter import *

master = Tk()

v = StringVar()
e = Entry(master, textvariable=v)
e.pack()

v.set('a default value')
s = v.get()

mainloop()