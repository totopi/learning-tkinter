# Standard widget used to input and/or output a single line of text
# To enter multiple lines, use the Text widget
from tkinter import *

master = Tk()
e = Entry(master)
e.pack()

# To add text, use insert, but first use a delete to replace current text
# e.delete(0, END)
e.insert(0, 'a default value')

# To fetch the current value, use the get method:
s = e.get()

mainloop()