from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.iconbitmap("C:/Users/User/Desktop/gui/photos/python_logo.ico")
root.title("Class Based GUI")
root.geometry("400x400")


class StartClass:
    """A parent class for the other classes in cgui.py"""
    def __init__(self, main):
        myFrame = Frame(main)
        myFrame.grid(row=0, column=0, columnspan=100)

        # the buttons

        self.button_back = Button(root, text="<<")
        # self.button_back = Button(root, text="<<", command=back(frame_number))
        self.button_back = Button(root, text="<<")
        self.button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
        # self.button_forward = Button(root, text=">>", command=lambda: forward(frame_number))
        self.button_forward = Button(root, text=">>")
        self.button_forward = Button(root, text=">>")

        self.button_back.grid(row=10, column=0, padx=60)
        self.button_exit.grid(row=10, column=1)
        self.button_forward.grid(row=10, column=3, padx=60)

        # the entry widget
        self.e = Entry(root, width=50, borderwidth=5)
        self.e.grid(row=0, column=0, columnspan=11)

        # submit button
        # self.sButton = Button(root, text="Enter Some Text")
        self.sButton = Button(root, text="Enter Some Text", command=self.myClick)
        self.sButton.grid(row=5, column=1)

    def myClick(self):
        #                   concatenation of strings
        myLabel = Label(root, text=self.e.get())
        myLabel.grid(row=30, column=1)



# class Frame5(StartClass):
#     """Display the text entered in Frame 1"""
#
#     def myClick(self):
#         #                   concatenation of strings
#         myLabel = Label(root, text="Hello " + self.e.get() + "!")
#         myLabel.grid(row=10, column=1, padx=50)


# class Frame2(StartClass):
#     """A class to open a picture + a button to open that picture"""
#
#     def __init__(self):
#         super(Frame2, self).__init__(self)
#
#
#     def open(self):
#         global myImage
#         root.filename = filedialog.askopenfilename(initialdir="C:/Users/User/Desktop/gui/photos", title="Select a file",
#                                                    filetypes=(("jpg files", "*.png"), ("all files", "*.*")))
#
#         myLabel = Label(root, text=root.filename).pack()
#
#         myImage = ImageTk.PhotoImage(Image.open(root.filename))
#         my_img_label = Label(image=myImage).pack()
#
#     my_btn = Button(root, text="Open File", command=open).pack()



a1 = StartClass(root)


root.mainloop()
