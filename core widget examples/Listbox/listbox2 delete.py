# Select from a group of textual items
# make it and then insert an index and string
from tkinter import *

master = Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, 'a list entry')

for item in ['one', 'two', 'three', 'four']:
    listbox.insert(END, item)

# To remove items from a list, use the delete method
# The most common usage is to clear the list (also needs to be done when updating the list)
listbox.delete(0, END)
for item in ['dog', 'cat', 'potato', 'banana']:
    listbox.insert(END, item)

# Can also delete one at a time, like in this example of a button that deletes an item from the list:
b = Button(master, text="Delete",
           command=lambda listbox=listbox: listbox.delete(ANCHOR))
b.pack()


mainloop()