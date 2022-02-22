from tkinter import *
from master import *
from start import *
# from show import *
# from welcome import *
# from register import *

class ButtonApp(Tk, Master):


    def __init__(self):
        super().__init__()
        Start()

if __name__ == "__main__":
    app = ButtonApp()
    app.geometry("300x300+810+390")
    app.resizable(False, False)
    # app.attributes('-fullscreen', True)
    app.title('Math Quiz')
    app.mainloop()