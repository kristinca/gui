import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image



class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(" An attempt to switch frames. ")
        self.geometry("400x400")
        self.iconbitmap('photos/python_logo.ico')
        self.resizable(width=True, height=True)

        container = tk.Frame(self)
        container.pack(side="top", fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.app_data = {"text": tk.StringVar(),
                         "clicked": tk.StringVar(),
                         "options": [
                                    "Monday",
                                    "Tuesday",
                                    "Wednesday",
                                    "Thursday",
                                    "Friday",
                                    "Saturday",
                                    "Sunday"
                                    ]
                        }

        self.frames = dict()

        for f in (FrameOne, FrameTwo, FrameThree, FrameFour, FrameFive):
            frame_name = f.__name__
            frame = f(parent=container, controller=self)
            self.frames[frame_name] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame("FrameOne")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

    def show(self, clicked):
        myLbl = ttk.Label(self, text=clicked.get())
        myLbl.pack()

class FrameOne(tk.Frame):
    """Enter some text in the entry widget"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.text = tk.StringVar()
        label1 = tk.Label(self, text='Frame One')
        label1.pack(side="bottom", fill='x')
        # label1.grid(row=0, column=1, sticky=(tk.W + tk.E))

        self.some_entry = ttk.Entry(self,
                                    textvariable=self.controller.app_data["text"])
        self.some_entry.pack()

        self.button1 = ttk.Button(self, text='<<', state='disabled')
        self.button1.pack(side='left')
        button2 = ttk.Button(self, text='>>', command=lambda: controller.show_frame('FrameTwo'))
        button2.pack(side='right')


        # self.myLabel.text = str(text)
        # button1.grid(row=1, column=2,
        # sticky=tk.W)
        # button2.grid(row=1, column=0, sticky=tk.E)


class FrameTwo(tk.Frame):
    """Open an image"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.my_btn = ttk.Button(self, text="Open File", command=self.open1)
        self.my_btn.pack()

        self.canvas = tk.Canvas(self, width=300, height=300)

        # self.canvas.pack()
        self.canvas.pack(fill=tk.BOTH, expand=-1)
        self.image = None

        label1 = tk.Label(self, text='Frame Two')
        # label1.grid(row=0, column=1, sticky=(tk.W + tk.E))
        label1.pack(side="bottom", fill='x')

        button1 = ttk.Button(self, text='<<', command=lambda: controller.show_frame('FrameOne'))
        button1.pack(side='left')

        button2 = ttk.Button(self, text='>>', command=lambda: controller.show_frame('FrameThree'))
        button2.pack(side='right')

    def open1(self):

        filename = tk.filedialog.askopenfilename(initialdir="C:/Users/User/Desktop/gui/photos",
                                                       title="Select a file",
                                                       filetypes=(("jpg files", "*.png"), ("all files", "*.*")))

        load = Image.open(filename)

        # basic resize, not packing the image on canvas
        # load = Image.open(filename).resize

        h, w = load.size
        self.render = ImageTk.PhotoImage(load)

        self.image = self.canvas.create_image(0, 0, image=self.render, anchor='nw')

        #     my_img_label = tk.Label(image=myImage)
        #     my_img_label.pack()
        # self.geometry("%dx%d" % (w, h))

        # self.canvas.pack()

    #     myLabel = tk.Label(self, text=self.filename)
    #     myLabel.pack()
    #
    #     myImage = ImageTk.PhotoImage(Image.open(self.filename))
    #     my_img_label = tk.Label(image=myImage)
    #     my_img_label.pack()

        # button1.grid(row=1, column=2, sticky=tk.W)
        # button2.grid(row=1, column=0, sticky=tk.E)


class FrameThree(tk.Frame):
    """Select a value from a drop down menu"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        label1 = tk.Label(self, text='Frame Three')
        label1.pack(side="bottom", fill='x')
        # label1.grid(row=0, column=1, sticky=(tk.W + tk.E))

        self.controller.app_data["clicked"].set(self.controller.app_data["options"][0])

        drop = tk.OptionMenu(self, self.controller.app_data["clicked"], *self.controller.app_data["options"])
        drop.pack()

        self.button1 = ttk.Button(self, text='<<', command=lambda: controller.show_frame('FrameTwo'))
        self.button1.pack(side='left')
        button2 = ttk.Button(self, text='>>', command=lambda: controller.show_frame('FrameFive'))
        button2.pack(side='right')


class FrameFour(tk.Frame):
    """Select a value from a drop down menu"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        label1 = tk.Label(self, text='Frame Four')
        label1.pack(side="bottom", fill='x')
        # label1.grid(row=0, column=1, sticky=(tk.W + tk.E))

        myBtn = ttk.Button(self, text="Show Selection",
                           command=lambda: self.controller.show(self.controller.app_data["clicked"]))
        myBtn.pack(side='top')

        self.button1 = ttk.Button(self, text='<<', command=lambda: controller.show_frame('FrameThree'))
        self.button1.pack(side='left')
        button2 = ttk.Button(self, text='>>', command=lambda: controller.show_frame('FrameFive'))
        button2.pack(side='right')


class FrameFive(tk.Frame):
    """Show the entered text from Frame One"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.text = tk.StringVar()

        label1 = tk.Label(self, text='Frame Five')
        label1.pack(side="bottom", fill='x')
        # label1.grid(row=0, column=1, sticky=(tk.W + tk.E))

        button1 = ttk.Button(self, text='<<', command=lambda: self.controller.show_frame('FrameFour'))
        button1.pack(side='left')

        button2 = ttk.Button(self, text='>>', state='disabled')
        button2.pack(side='right')

        # button1.grid(row=1, column=2, sticky=tk.W)
        # button2.grid(row=1, column=0, sticky=tk.E)
        self.myLabel = ttk.Label(self, textvariable=self.text)
        self.myLabel.pack()
        button3 = ttk.Button(self, text='Show text', command=lambda: self.print_it())
        button3.pack()

    def print_it(self):
        self.text.set(self.controller.app_data["text"].get())
        print(self.text)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
