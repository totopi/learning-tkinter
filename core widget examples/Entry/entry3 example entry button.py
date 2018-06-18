# Creates an entry widget, and a button that prints the current contents
from tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set() # This sets the cursor to start here?

def callback():
    print(e.get())
    
b = Button(master, text='get', width=10, command=callback)
b.pack()

mainloop()

e = Entry(master, width=50)
e.pack()

text = e.get()