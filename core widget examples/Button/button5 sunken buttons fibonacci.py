# Will look like it's held
# Just change relief from RAISED to SUNKEN
from tkinter import *

master = Tk()

# Lets make a generator to spit out fibonnaci numbers
def fib_gen():
    first, second = 0, 1
    while True:
        yield second
        first, second = second, first + second

fib_num = fib_gen()

# And a little callback to print them out
def fibonacci():
    global fib_num
    print(next(fib_num))
    
b = Button(master, text = 'Hay', command=fibonacci)
b.config(relief=SUNKEN)
b.pack()

mainloop()