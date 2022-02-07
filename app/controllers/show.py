from tkinter import *


def frame_basic():
    return Frame()


class Show:

    def __init__(self):

        self.f1 = frame_basic()
        self.f1.grid()
        Label(self.f1, text='First Frame').grid(row=0, column=0, columnspan=3, pady=10, sticky='WE')
        Button(self.f1, text="click me", command=lambda: self.replace_with(10)).grid(row=1, column=0)
        Button(self.f1, text="click me", command=lambda: self.replace_with(20)).grid(row=1, column=1)
        Button(self.f1, text="click me", command=lambda: self.replace_with(30)).grid(row=1, column=2)

    def replace_with(self, value=0):
        self.f1.destroy()
        self.f1 = frame_basic()
        self.f1.grid(sticky=NSEW)
        Label(self.f1, text="Second Frame").grid(row=0, column=0, columnspan=3, pady=10, sticky='WE')
        Button(self.f1, text=value, command=self.back_to_start).grid(row=1, column=0)
        Button(self.f1, text=value + 10, command=self.back_to_start).grid(row=1, column=2)
        Button(self.f1, text=value + 20, command=self.back_to_start).grid(row=1, column=1)

    def back_to_start(self):
        self.f1.destroy()
        Show()
