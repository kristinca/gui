from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("a title")
root.iconbitmap('photos/python_logo.ico')
root.geometry("400x200")


def graph():
    house_prices =  np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

myBtn = Button(root, text="Graph it!", command=graph)
myBtn.pack()


root.mainloop()
