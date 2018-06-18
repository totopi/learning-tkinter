# This has a function, yay  I guess you can use this as a password entry and have the stringvar be gotten from a checkbutton or w/e
from tkinter import *

parent = Tk()

def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

caption = 'Words'

user = makeentry(parent, 'User name:', 10)
password = makeentry(parent, 'Password:', 10, show='*')
content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)
entry.pack()

text = content.get()
content.set(text)
mainloop()
