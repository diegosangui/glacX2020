from funcs.modulos import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.labelStyle import LabelGlac
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *

class Aba4:
    def aba4(self):
        ###Frames da moldura
        self.frameProb = GradientFrame(self.frame_aba4)
        self.frameProb.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        # Tanque de combustivel
        descrTanq = LabelGlac(self.frame_aba4)
        descrTanq.configure(width=22, text=self.m_Tanque)
        descrTanq.place(relx=0.02, rely=0.1, relwidth=0.21, relheight=0.1)

        self.are1 = Entry(self.frame_aba4)
        self.are1.place(relx=0.23, rely=0.1,
                        relwidth=0.18, relheight=0.1)

        # Odometro
        descrOdom = LabelGlac(self.frame_aba4)
        descrOdom.configure(text=self.m_Odometro)
        descrOdom.place(relx=0.02, rely=0.22,
                        relwidth=0.21, relheight=0.1)

        self.are2 = Entry(self.frame_aba4)
        self.are2.place(relx=0.23, rely=0.22,
                        relwidth=0.18, relheight=0.1)

        ###  Radio Kit Multimidia
        descrRad = LabelGlac(self.frame_aba4)
        descrRad.configure(text=self.m_Obs)
        descrRad.place(relx=0.05, rely=0.34, relwidth=0.18, relheight=0.1)

        self.are3 = Entry(self.frame_aba4)
        self.are3.place(relx=0.23, rely=0.34,
                        relwidth=0.18, relheight=0.1)

        ####   Calotas
        descrCalot = LabelGlac(self.frame_aba4)
        descrCalot.configure(text=self.m_Obs)
        descrCalot.place(relx=0.05, rely=0.46,
                         relwidth=0.18, relheight=0.1)

        self.are4 = Entry(self.frame_aba4)
        self.are4.place(relx=0.23, rely=0.46,
                        relwidth=0.18, relheight=0.1)

        ####  Triangulo
        descrtri = LabelGlac(self.frame_aba4)
        descrtri.configure(text=self.m_Obs)
        descrtri.place(relx=0.05, rely=0.58, relwidth=0.18, relheight=0.1)

        self.are5 = Entry(self.frame_aba4)
        self.are5.place(relx=0.23, rely=0.58,
                        relwidth=0.18, relheight=0.1)

        ###   Macaco
        descrMacaco = LabelGlac(self.frame_aba4)
        descrMacaco.configure(text=self.m_Obs)
        descrMacaco.place(relx=0.05, rely=0.7, relwidth=0.18, relheight=0.1)

        self.are6 = Entry(self.frame_aba4)
        self.are6.place(relx=0.23, rely=0.7,
                        relwidth=0.18, relheight=0.1)

        ####   Estepe
        descrEst = LabelGlac(self.frame_aba4)
        descrEst.configure(text=self.m_Obs)
        descrEst.place(relx=0.05, rely=0.82, relwidth=0.18, relheight=0.1)

        self.are7 = Entry(self.frame_aba4)
        self.are7.place(relx=0.23, rely=0.82,
                        relwidth=0.18, relheight=0.1)

        ####   Are 8
        descrAre8 = LabelGlac(self.frame_aba4)
        descrAre8.configure(text=self.m_Obs)
        descrAre8.place(relx=0.55, rely=0.1,
                        relwidth=0.18, relheight=0.1)

        self.are8 = Entry(self.frame_aba4)
        self.are8.place(relx=0.73, rely=0.1,
                        relwidth=0.18, relheight=0.1)

        ####   Are 9
        descrAre9 = LabelGlac(self.frame_aba4)
        descrAre9.configure(text=self.m_Obs)
        descrAre9.place(relx=0.55, rely=0.22,
                        relwidth=0.18, relheight=0.1)

        self.are9 = Entry(self.frame_aba4)
        self.are9.place(relx=0.73, rely=0.22,
                        relwidth=0.18, relheight=0.1)

        # Gerar PDF
        vistlabel = LabelGlac(self.frame_aba4)
        vistlabel.configure(text=self.m_ImprimirVistoria)
        vistlabel.place(relx=0.61, rely=0.61, width= 220, height= 25)

        ###  Botao botaoImprimirVist
        self.botaoImprimirVist = Button(self.frame_aba4,
            image=self.button_imprime2, command=self.imprime_vist)
        self.botaoImprimirVist.place(relx=0.69, rely=0.43,
                                     width= 72, height= 47)
