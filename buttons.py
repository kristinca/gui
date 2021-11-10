from tkinter import *


root = Tk()


def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

# myButton = Button(root, text="Click me!", state=DISABLED, padx=50)
# padx -> horizontal, pady -> vertical
# myButton = Button(root, text="Click me!", padx=50, pady=50)
# myButton = Button(root, text="Click me!", command=myClick)
# hex color codes -> fg, bg ...
myButton = Button(root, text="Click me!", command=myClick, fg="blue", bg="#00FF00")

myButton.pack()

root.mainloop()
