# Labels are used to display text and images
# Uses double buffering, so it can be updated at any time without pesky flickering
# To display data for users to manipulate, one may wish to consider Canvas widgets
#
# To use a label, just specify what to display in it (text, bitmap, or image)
from tkinter import *
from PIL import Image, ImageTk

master = Tk()
longtext = 'Hello this is an awful lot of text, dont you just love how much text there is in this long text box?  I know that I do, all this text, just texting everywhere, not really doing anything except being a text...'
# Basic basic call
# w = Label(master, text='Hello, world!')
# can use height or width for size, fg for text color, font  to choose your font
# w = Label(master, text="Rouge", fg="red")
# w = Label(master, text="Helvetica", font=("Helvetica", 16))
# can also wrap text
w = Label(master, text=longtext, wraplength=100, anchor=W, justify=LEFT)
w.pack()

# Can also use variables for the text, label automatically updates when the text does.
v = StringVar()
Label(master, textvariable=v).pack()

# Also to do pictures, but make sure to keep a reference to the image object, otherwise it will be garbage collected
# Use a global variable or instance attribute or just add an attribute to the widget instance like so:
pachi = Image.open('pachi.png')
photo = ImageTk.PhotoImage(pachi)
x = Label(master, image=photo)
x.photo = photo
x.pack()

v.set("New Text!")

mainloop()