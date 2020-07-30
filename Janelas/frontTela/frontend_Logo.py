from funcs.modulos import *
from Janelas.estiloWidgets.autcomplety import *

class Logotipo:
    def logotipo(self):
        self.textoLogo = Label(self.top, bg='#49708D', text=self.m_logorf, bd=0,
                fg=self.bg_label, font=('Comic', '24', 'bold'))
        self.textoLogo.place(relx=0.8, rely=0.2, relwidth=0.15, relheight=0.6)
        progress1 = ttk.Progressbar(self.top, orient=HORIZONTAL, length=100,
                                    mode='indeterminate')
        progress1.place(relx=0.8, rely=0.2, relwidth=0.15, relheight=0.05)
        progress1.start(10)
