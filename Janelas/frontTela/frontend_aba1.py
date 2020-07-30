from funcs.modulos import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.labelStyle import LabelGlac
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *

class Aba1:
    def aba1(self):
        ####  Descrição dos problemas apresentados pelo veiculo - Aba 1
        self.frameProb = GradientFrame(self.frame_aba1, relief=SUNKEN)
        self.frameProb.place(relx=0, rely=0.01, relwidth=1, relheight=1)

        self.DescrProb = LabelGlac(self.frame_aba1)
        self.DescrProb.configure(text= "   " + self.m_Atend1)
        self.DescrProb.place(relx=0.04, rely=0.04, relwidth=0.91, relheight=0.12)

        self.area1 = Entry(self.frame_aba1)
        self.area1.place(relx=0.05, rely=0.2,
                         relwidth=0.9, relheight=0.1)

        self.area2 = Entry(self.frame_aba1)
        self.area2.place(relx=0.05, rely=0.35,
                         relwidth=0.9, relheight=0.1)

        self.DescrProb2 = LabelGlac(self.frame_aba1)
        self.DescrProb2.configure(text="   " + self.m_Atend2)
        self.DescrProb2.place(relx=0.04, rely=0.49,
                              relwidth=0.91, relheight=0.12)

        self.area3 = Entry(self.frame_aba1)
        self.area3.place(relx=0.05, rely=0.65,
                         relwidth=0.9, relheight=0.1)

        self.area4 = Entry(self.frame_aba1)
        self.area4.place(relx=0.05, rely=0.8,
                         relwidth=0.9, relheight=0.1)

        ###  Label e Entrada Inicio
        self.hoje = str(self.hj.day) + '/' + str(self.hj.month) + '/' + str(self.hj.year)

        self.descrInicio = Button(self.frame_aba1, font=('Verdana', '8', 'bold'),
            command =self.calendarioInicio)
        self.descrInicio.configure(text='Data inicial',
                                   fg=self.fg_label,
                                   bg=self.fundo_do_frame)
        self.descrInicio.place(relx=0.05, rely=0.045,
                               relwidth=0.08, relheight=0.1)

        self.listInicio = EntPlaceHold(self.frame_aba1, self.hoje )
        self.listInicio.place(relx=0.14, rely=0.045,
                              relwidth=0.08, relheight=0.1)

        ###  Label e Entrada Fim
        self.descrFim = Button(self.frame_aba1, font=('Verdana', '8', 'bold'),
            command=self.calendarioFim);
        self.descrFim.configure(text='Data final', fg=self.fg_label,
            bg=self.fundo_do_frame)
        self.descrFim.place(relx=0.05, rely=0.495, relwidth=0.08, relheight=0.1)

        self.listFim = EntPlaceHold(self.frame_aba1, self.hoje)
        self.listFim.place(relx=0.14, rely=0.495, relwidth=0.08, relheight=0.1)