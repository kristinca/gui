import tkinter as tk
from tkinter import ttk


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

        self.frames = dict()

        for f in (FrameOne, FrameTwo, FrameThree):
            frame_name = f.__name__
            frame = f(parent=container, controller=self)
            self.frames[frame_name] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame("FrameOne")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()


class FrameOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        label1 = tk.Label(self, text='Frame One')
        label1.pack(side="top", fill='x')
        # label1.grid(row=0, column=1, sticky=(tk.W + tk.E))

        button1 = ttk.Button(self, text='-> FrameTwo', command=lambda: controller.show_frame('FrameTwo'))
        button1.pack(side='left')
        button2 = ttk.Button(self, text='-> Frame Three', command=lambda: controller.show_frame('FrameThree'))
        button2.pack(side='right')

        # button1.grid(row=1, column=2, sticky=tk.W)
        # button2.grid(row=1, column=0, sticky=tk.E)


class FrameTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        label1 = tk.Label(self, text='Frame Two')
        label1.grid(row=0, column=1, sticky=(tk.W + tk.E))
        label1.pack(side="top", fill='x')

        button1 = ttk.Button(self, text='-> Frame One', command=lambda: controller.show_frame('FrameOne'))
        button1.pack(side='left')

        button2 = ttk.Button(self, text='-> Frame Three', command=lambda: controller.show_frame('FrameThree'))
        button2.pack(side='right')

        # button1.grid(row=1, column=2, sticky=tk.W)
        # button2.grid(row=1, column=0, sticky=tk.E)


class FrameThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        label1 = tk.Label(self, text='Frame Three')
        label1.pack(side="top", fill='x')
        # label1.grid(row=0, column=1, sticky=(tk.W + tk.E))

        button1 = ttk.Button(self, text='-> Frame One', command=lambda: self.controller.show_frame('FrameOne'))
        button1.pack(side='left')

        button2 = ttk.Button(self, text='-> Frame Two', command=lambda: self.controller.show_frame('FrameTwo'))
        button2.pack(side='right')

        # button1.grid(row=1, column=2, sticky=tk.W)
        # button2.grid(row=1, column=0, sticky=tk.E)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
