# Dependencies
from tkinter import *

# Must declare a root widget, this is the main window, should have only one and declare it before anything else.
root = Tk()

# Create a Label widget as a child to the root window
w = Label(root, text="Hello, world!") # a label can have text or icon / image
w.pack() # pack will size it to fit its contents and make it visible

# The window won't appear until we've entered the Tkinter event loop
root.mainloop() # Program stays in the main loop until the window is closed
# handles events from user (mouse clicks, key presses)
# events from windowing system (redraws, config msgs)
# operations queued by Tkinter - geometry shenanigans (pack) and display updates
# app window doesn't appear until this is run!