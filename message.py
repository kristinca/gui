from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title('some title')
root.iconbitmap('photos/python_logo.ico')

# types of messagebox:
# showinfo
# showwarning
# showerror
# askquestion
# askokcalcel
# askyesno


def popup():
    # messagebox.showinfo("This is a popup", "Hello World!")
    # messagebox.showwarning("This is a popup", "Hello World!")
    # messagebox.showerror("This is a popup", "Hello World!")
    # messagebox.askquestion("This is a popup", "Hello World!")
    # messagebox.askokcancel("This is a popup", "Hello World!")
    response = messagebox.askyesno("This is a popup", "Hello World!")
    # Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes").pack()
    else:
        Label(root, text="You clicked no").pack()


Button(root, text="popup", command=popup).pack()


mainloop()