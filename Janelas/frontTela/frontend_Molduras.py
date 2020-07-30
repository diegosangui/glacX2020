from funcs.modulos import *
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *

class Molduras:
    def molduras(self):
        ### Moldura dos dados do cliente
        self.FrameCliente = Frame(self.top2, bg="#C6CCFF", relief="sunken")
        self.FrameCliente.place(relx=0, rely=0, relwidth=0.47, relheight=1)
        ### Lista das placas de veiculos do cliente
        self.FrameAut2 = Frame(self.top2, width=10, bg=self.fundo_do_frame, bd=1, highlightbackground=self.borda_frame,
                               highlightthickness=3);
        self.FrameAut2.place(relx=0.465, rely=0.002, relwidth=0.1, relheight=1)
        ### Moldura dos dados veiculo
        self.FrameAut = Frame(self.top2, bg="#C6CCFF", relief="sunken");
        self.FrameAut.place(relx=0.56, rely=0.002, relwidth=0.44, relheight=1)

        self.FrameAbas = GradientFrame(self.top3, borderwidth=1, relief="sunken");
        self.FrameAbas.place(relx=0, rely=0, relwidth=1, relheight=1)
        ######################
        self.FrameTec = GradientFrame(self.top4, borderwidth=1, relief="sunken");
        self.FrameTec.place(relx=0, rely=0, relwidth=1, relheight=1)
        ######################
