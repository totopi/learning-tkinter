# The most basic of buttons
# declare the Tk thingamy, then declare our button with the function callback
# Which will print 'click!' on the terminal

from tkinter import *

master = Tk()

def callback():
    print('click!')

b = Button(master, text='OK', command=callback)
b.pack()

mainloop()