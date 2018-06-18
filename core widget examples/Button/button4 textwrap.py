# Buttons can display multiple lines of text, in only one font though
# Use newlines, or wraplength kwarg/option to make the button wrap text by itself
# When wrapping text, use anchor, justify, or maybe even padx kwarg/option to make things look how you want
# Ex:

from tkinter import *

master = Tk()
longtext = 'Hello this is a bunch of text \nthat is quite long to fit onto \na button, isnt it!'
b = Button(master, text=longtext, anchor=W, justify=LEFT, padx=2)
b.pack()

mainloop()