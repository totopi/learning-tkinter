# Select from a group of textual items
# make it and then insert an index and string
from tkinter import *

master = Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, 'a list entry')

for item in ['one', 'two', 'three', 'four']:
    listbox.insert(END, item)

mainloop()