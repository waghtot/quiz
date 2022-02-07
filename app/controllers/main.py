from tkinter import *
from show import *


class ButtonApp(Tk):

    def __init__(self):
        super().__init__()
        Show()


if __name__ == "__main__":
    app = ButtonApp()
    app.geometry("300x300+810+390")
    app.resizable(False, False)
    # app.attributes('-fullscreen', True)
    app.title('Math Quiz')
    app.mainloop()