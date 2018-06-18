# Checkbuttons are used for on-off selections
# Can contain text or images, and can associate a function with each button
# One character can be underlined, to indicate a keyboard shortcut or so
# By default, tab key can be used to move it
# Should be associated with a variable!

# Use to select on or off, many-of-many
# If you want to do one-of-many, use Radiobuttons or Listbox widget
from tkinter import *

master = Tk()
var = IntVar()

c = Checkbutton(master, text='Expand', variable=var)
c.pack()

mainloop()