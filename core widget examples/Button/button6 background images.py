# Background can also be changed
# Might be better to use a Checkbutton or Radiobutton with indicatoron set to false?
from tkinter import *
from PIL import Image, ImageTk

master = Tk()
im = Image.open('pachi.png')
ph = ImageTk.PhotoImage(im)
var = IntVar()
b = Button(master, image=ph) # using a button
# b = Checkbutton(master, image=ph, variable=var, indicatoron=0) # using a checkbutton
b.pack()

mainloop()