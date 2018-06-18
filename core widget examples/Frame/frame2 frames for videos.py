# A frame widget can also be used as a placeholder for video overlays and other external processes
# To do so, set the background color to an empty string (prevents updates, and leaves the color map alone)
# pack as usual, and use the window_id method to get the window handle corresponding to the frame
from tkinter import *

master = Tk()

frame = Frame(width=768, height=576, bg='', colormap='new')
frame.pack()

video.attach_window(frame.window_id())

mainloop()