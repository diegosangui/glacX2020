from tkinter import *

class ButtonGlac(Button):
    def __init__(self, master=None):
        super().__init__(master)

        self.configure(
            bd=1,
            bg='#49708D',
            fg= 'white',
            font=('Aharoni','10','bold'),
            activebackground = '#278ab9',
            activeforeground= "lightgray"
        )





