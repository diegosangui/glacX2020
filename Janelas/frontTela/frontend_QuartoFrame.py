from funcs.modulos import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.autcomplety import *
from Janelas.estiloWidgets.labelStyle import *

class QuartoFrame:
    def quarto_frame(self):
        #### Tecnico de reparo
        self.lbTecnico = LabelGlac(self.FrameTec)
        self.lbTecnico.configure(text= 'Tecnico')
        self.lbTecnico.place(relx=0.005, rely=0.1,
                                  relwidth=0.15, relheight=0.4)

        self.entradaTecnico = Entry(self.FrameTec)
        self.entradaTecnico.place(relx=0.005, rely=0.5,
                                  relwidth=0.15, relheight=0.4)

        self.tecnicoBt = self.tecnicoBt.subsample(12,12)
        self.botaotec = Button(self.FrameTec, image=self.tecnicoBt, bd=0,
            command=self.busca_tecnico)
        self.botaotec.place(relx=0.16, rely=0.15,
                            width= 37, height= 33);

        ##### label e listbox do numero do orcamento
        self.listaNumOrc = Entry(self.FrameTec)
        self.listaNumOrc.place(relx=0.325, y=8,
                               relwidth=0.08, relheight=0.6)

        ###  Botao Gravar
        self.gravarBt = self.gravarBt.subsample(3,3)
        self.botaoAbreOrc = Button(self.FrameTec, bd=0,image= self.gravarBt,
            command=self.abre_orc)
        self.botaoAbreOrc.place(relx=0.41, y=5, width= 47, height=32)

        ###  Botao Buscar
        self.buscarBt = self.buscarBt.subsample(3,3)
        self.botaoCarregaOrc = Button(self.FrameTec, bd=0, image= self.buscarBt,
            command = self.busca_orc)
        self.botaoCarregaOrc.place(relx=0.46, y=5, width= 47, height=32)

        ### Botao Alterar
        self.alterarBt = self.alterarBt.subsample(3,3)
        self.botaoAlteraOrc = Button(self.FrameTec, bd=0, image= self.alterarBt, command=self.altera_orc)
        self.botaoAlteraOrc.place(relx=0.51, y=5, width= 47, height=32)

        ############################################################################################################################
        ##  Entrada Total
        self.entradatotal = Entry(self.FrameTec)
        self.entradatotal.place(relx=0.86, rely=0.3,
                                relwidth=0.12, relheight=0.5);
        self.entradatotal2 = Entry(self.FrameTec)

        ## Botao Total
        self.descrtotal = ButtonGlac(self.FrameTec)
        self.descrtotal.configure(text=self.m_Total, command=self.total_orc)
        self.descrtotal.place(relx=0.75, rely=0.25, relwidth=0.1, relheight=0.6)
