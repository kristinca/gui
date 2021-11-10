from tkinter import *



# to create anything in tkinter :
# 1. define the thing we created
# 2. put it up on the screen

root = Tk()

# create a label widget


# # 1 step :
# myLabel1 = Label(root, text="Hello, world!").grid(row=0, column=0)
# myLabel2 = Label(root, text="Hello tkinter!").grid(row=1, column=5)
# myLabel3 = Label(root, text="             ").grid(row=1, column=1)


# 2 step:
myLabel1 = Label(root, text="Hello, world!")
myLabel2 = Label(root, text="Hello tkinter!")
myLabel3 = Label(root, text="             ")

# put it on the screen
# pack => pack everything just as big as it is
# myLabel.pack()

myLabel1.grid(row=0, column=0)
# columns are relative to each other
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)

root.mainloop()
