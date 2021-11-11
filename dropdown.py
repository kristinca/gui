from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("a title")
root.iconbitmap("photos/python_logo.ico")
root.geometry("400x400")

# Drop Down boxes
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

clicked = StringVar()
# clicked.set("Monday")
clicked.set(options[0])


def show():
    myLbl = Label(root, text=clicked.get()).pack()


drop = OptionMenu(root, clicked, *options)
drop.pack()

myBtn = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
