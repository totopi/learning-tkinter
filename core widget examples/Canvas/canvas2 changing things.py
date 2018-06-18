# Items are kept on the canvas until you remove them
# Use methods like coords, itemconfig, and move to modify things
# And delete to remove things
# Of course, things must be saved to variables before they can be modified!
from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

xy = (0, 50, 200, 50)
i = w.create_line(xy, fill="red")
new_xy = (10, 50, 190, 50)
w.coords(i, new_xy) # change coordinates
w.itemconfig(i, fill="blue") # change color
w.delete(i) # remove

# w.delete(ALL) # remove all items

mainloop()