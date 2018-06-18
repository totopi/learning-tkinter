# padx and pady kwargs/options can give it some space between other elements
# height and width kwargs/options explicity set the size in text units if contents is text, otherwise pixels
# Here is one example of how to set the size in pixels even though the contents are text, there are many more
from tkinter import Tk, Frame, Button, BOTH, mainloop

master = Tk()

f = Frame(master, height=62, width=62)
f.pack_propagate(0) # don't shrink
f.pack()

b = Button(f, text = 'Sure!')
b.pack(fill=BOTH, expand=1)

mainloop()