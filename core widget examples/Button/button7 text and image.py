# If you use text and image, only the image will show
# Use the extra option compound to do so
# set compound = CENTER to display text on top of an image
# To display an icon along with text, set the option to LEFT, RIGHT, TOP, or BOTTOM
from tkinter import *
from PIL import Image, ImageTk

master = Tk()
im  = Image.open('pachi.png')
ph = ImageTk.PhotoImage(im)

# b = Button(master, image=ph, text='Click me!', compound=CENTER)
# b = Button(master, compound=LEFT, image=ph, text='Action') # Icon to the left of the text label
b = Button(master, compound=TOP, image=ph, text="Quit") # Icon on top of the label
b.pack()

mainloop()