"""Creating input fields"""

from tkinter import *

root = Tk()

# e = Entry(root, width=50, bg='green', fg='white')

e = Entry(root, width=50, borderwidth=5)
e.pack()

# default text inside of the box
e.insert(0, "Enter Your Name: ")


def myClick():
    #                   concatenation of strings
    myLabel = Label(root, text="Hello "+e.get()+"!")
    myLabel.pack()


myButton = Button(root, text="Enter Your Name", command=myClick)

myButton.pack()

root.mainloop()
