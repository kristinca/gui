from tkinter import *



# to create anything in tkinter :
# 1. define the thing we created
# 2. put it up on the screen

root = Tk()

# create a label widget
myLabel = Label(root, text="Hello, world!")

# put it on the screen
myLabel.pack()

root.mainloop()
