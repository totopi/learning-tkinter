# Select from a group of textual items
# make it and then insert an index and string
from tkinter import *

master = Tk()

listbox = Listbox(master, selectmode=EXTENDED)
listbox.pack()

listbox.insert(END, 'a list entry')

for item in ['one', 'two', 'three', 'four']:
    listbox.insert(END, item)

mainloop()

# Four different types are available through selectmode option
# SINGLE: just one choice
# BROWSE: selection can be moved using the mouse
# MULTIPLE: clicking chooses more than one item
# EXTENDED: multiple ranges of items can be chosen, using shift and control