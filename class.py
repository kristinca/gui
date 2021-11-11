from tkinter import *


root = Tk()
root.title("a title")
root.iconbitmap("photos/python_logo.ico")
root.geometry("400x400")


class Aclass:
    #          self, root=main root
    def __init__(self, main):
        myFrame = Frame(main)
        myFrame.pack()

        self.myBtn = Button(main, text="Click me!", command=self.clicker)
        self.myBtn.pack(pady=20)

    def clicker(self):
        print("this is a button")


a1 = Aclass(root)


root.mainloop()