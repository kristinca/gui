from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('a title')
root.iconbitmap('photos/python_logo.ico')

# r = IntVar()
# # r = StrVar()
# r.get()

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushrooms", "Mushrooms"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# # RadioButton(root, text='Option 1', variable=r, value="1").pack()
# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

# myLabel = Label(root, text=r.get())
myLabel = Label(root, text=pizza.get())
myLabel.pack()

# myButton = Button(root, text="Click me", command=lambda: clicked(r.get()))
myButton = Button(root, text="Click me", command=lambda: clicked(pizza.get()))
myButton.pack()

mainloop()