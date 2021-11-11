from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("a title")
root.iconbitmap("photos/python_logo.ico")

def show():
    myLabel = Label(root, text=var.get()).pack()



# var = IntVar()

var = StringVar()

c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

# myLabel = Label(root, text=var.get()).pack()

mybtn = Button(root, text="Show selection", command=show).pack()

mainloop(0)