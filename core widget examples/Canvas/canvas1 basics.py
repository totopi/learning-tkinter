# Basic pattern for a canvas
# Use a canvas for graphs, images, completion bars, etc!
# To draw things on a canvas, use create methods
from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100) # x1, y1, x2, y2
w.create_line(0, 100, 200, 0, fill='red', dash=(4, 4)) # dash is numpixels on and off?

w.create_rectangle(50, 25, 150, 75, fill='blue')

mainloop()