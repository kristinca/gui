from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("a title")
root.iconbitmap("photos/python_logo.ico")


def open():
    global my_image
    top = Toplevel()
    # lbl = Label(top, text="Hello, world").pack()
    top.title("a second window")
    top.iconbitmap("photos/python_logo.ico")
    my_image = ImageTk.PhotoImage(Image.open("photos/turtle.jpg"))
    my_label = Label(top, image=my_image).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text='open second window', command=open).pack()

mainloop()
