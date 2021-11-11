from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title("a title")
root.iconbitmap("photos/python_logo.ico")


def open():
    global myImage
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/User/Desktop/gui/photos", title="Select a file",
                                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))

    myLabel = Label(root, text=root.filename).pack()

    myImage = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label = Label(image=myImage).pack()


my_btn = Button(root, text="Open File", command=open).pack()

mainloop()