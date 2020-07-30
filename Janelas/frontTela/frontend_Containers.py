from funcs.modulos import *
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *

class Containers:
    def containers(self):
        ###     Primeiro Container da janela
        self.top = GradientFrame(self.janela, borderwidth=0, relief="sunken")
        self.top.place(relx=0.01, rely=0.005, relwidth=0.98, relheight=0.13)
        ### Segundo Container da Janela
        self.top2 = GradientFrame(self.janela, borderwidth=0, relief="sunken")
        self.top2.place(relx=0.01, rely=0.14, relwidth=0.98, relheight=0.2)
        ### Terceiro Container da janela
        self.top3 = Frame(self.janela, bd=1, bg=self.fundo_do_frame, highlightbackground=self.borda_frame,
                     highlightthickness=3);
        self.top3.place(relx=0.01, rely=0.35, relwidth=0.98, relheight=0.45)
        ### Quarto Container da Janela
        self.top4 = Frame(self.janela, width=95, bd=2, bg=self.fundo_do_frame, highlightbackground=self.borda_frame,
                     highlightthickness=3);
        self.top4.place(relx=0.01, rely=0.805, relwidth=0.98, relheight=0.09)
        ### Quinto Container da janela
        self.top5 = GradientFrame(self.janela, borderwidth=0, relief="sunken")
        self.top5.place(relx=0.01, rely=0.905, relwidth=0.98, relheight=0.09)
