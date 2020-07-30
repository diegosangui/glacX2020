from tkinter import *

class LabelGlac(Label):
    def __init__(self, master=None):
        super().__init__(master)

        self.configure(
            bd=0,
            bg='#89add6',
            fg= '#192e47',
            font=('Verdana', '10', 'bold'),
            activebackground = '#278ab9',
            activeforeground= "lightgray"
        )