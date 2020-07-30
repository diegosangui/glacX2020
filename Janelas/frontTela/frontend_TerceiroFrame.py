from funcs.modulos import *
from Janelas.estiloWidgets.autcomplety import *

class TerceiroFrame:
    def terceiro_frame(self):
        ##########################################################################################################
        ###  A B A S
        self.abas = ttk.Notebook(self.FrameAbas);
        self.frame_aba1 = Frame(self.abas);
        self.frame_aba2 = Frame(self.abas)
        self.frame_aba3 = Frame(self.abas);
        self.frame_aba4 = Frame(self.abas);
        self.frame_aba5 = Frame(self.abas)

        self.frame_aba1.configure(background=self.fundo_do_frame)
        self.frame_aba2.configure(background=self.fundo_do_frame)
        self.frame_aba4.configure(background=self.fundo_do_frame)
        self.frame_aba5.configure(background=self.fundo_do_frame)
        self.label1 = Label(self.frame_aba1);
        self.label1.pack(padx=850, pady=225)

        self.label3 = Label(self.frame_aba3);
        self.label3.pack(padx=850, pady=225)
        self.label4 = Label(self.frame_aba4);
        self.label4.pack(padx=850, pady=225)
        self.label5 = Label(self.frame_aba5);
        self.label5.pack(padx=850, pady=225)
        self.abas.add(self.frame_aba1, text=self.m_Aba3);
        self.abas.add(self.frame_aba2, text=self.m_Aba1)

        self.abas.add(self.frame_aba4, text=self.m_Aba4)
        # self.abas.add(self.frame_aba5, text=self.m_Aba5)
        self.abas.pack(side="bottom")
