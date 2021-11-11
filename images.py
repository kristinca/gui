from tkinter import *
from PIL import ImageTk, Image


# 1. define the image
# 2. put the image in something else
# 3. put that something else on the screen

root = Tk()
root.title("a title")
root.iconbitmap('photos/python_logo.ico')

my_img = ImageTk.PhotoImage(Image.open('photos/turtle1.png'))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()

root.mainloop()
