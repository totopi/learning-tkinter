from tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master) # The window!
        frame.pack() # Make it visible!

        self.button = Button(frame, text='QUIT', fg='red', command=frame.quit) # passing 'options' as kwargs: fg = foreground color, command = some kind of function or bound method
        self.button.pack(side=LEFT) # if no side is given, default value is top
        # Also you want to keep the declaration and pack separate, if you want to store it.  And you always want to store it as a variable unless you never ever need to see it again!
        self.hi_there = Button(frame, text='Hello', command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    # hello button callback
    def say_hi(self): 
        print('hi there, everyone!')

# instance the root widget
root = Tk()

# instance the app class with root as its parent
app = App(root)

root.mainloop()
root.destroy() # optional,