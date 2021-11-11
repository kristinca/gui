from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('some title')
root.iconbitmap('photos/python_logo.ico')

# frame = LabelFrame(root, text="This is a frame", padx=5, pady=5)
# frame = LabelFrame(root, text="This is a frame", padx=50, pady=50)
frame = LabelFrame(root, padx=50, pady=50)
# frame.pack(padx=10, pady=10)
frame.pack(padx=100, pady=100)

b = Button(frame, text="Don't Click Here")
b2 = Button(frame, text="... or Here")
b.pack()
b2.pack()

root.mainloop()
