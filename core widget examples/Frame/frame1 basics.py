# A frame is a rectangular region on the screen
# Used mainly as a geometry master for other widgets, or to provide padding
# Useful for grouping other widgets into complex layouts
# Useful for padding
# Useful as a base class for compound widgets
from tkinter import *

master = Tk()

Label(text='one').pack()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Label(text='two').pack()

mainloop()