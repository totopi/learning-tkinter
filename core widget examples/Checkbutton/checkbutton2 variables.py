# The variable can be an IntVar() as before, but does not have to be
# Can also be StringVar()
# But then you have to change
# onvalue
# offvalue
# Which otherwise default to 1 and 0, respectively
from tkinter import *

master = Tk()

var = StringVar()
c = Checkbutton(
    master, text='Color image', variable=var,
    onvalue='RGB', offvalue='L'
    )
# if you want to keep the variable attached to the widget, just do this!
c.var = var
c.pack()

mainloop()