from funcs.modulos import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.labelStyle import LabelGlac
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *
from funcs.backCads.backConsFinan import *

class Financeiro(ConsFinan):
    def cadfinan(self):
        self.janelaFin = Toplevel()
        self.janelaFin.configure(background=self.fundo_da_tela)
        self.janelaFin.title(self.m_Financeiro)
        self.janelaFin.geometry("777x335")
        self.janelaFin.resizable(FALSE, FALSE)
        self.janelaFin.transient(self.janela)
        self.janelaFin.focus_force()
        self.janelaFin.grab_set()

        ###  A B A S
        self.abas = Notebook(self.janelaFin)
        self.frame_aba1 = Frame(self.abas)
        self.frame_aba1.configure(background='gray75')

        self.label1 = Label(self.frame_aba1)
        self.label1.pack(padx=385, pady=160)
        self.abas.add(self.frame_aba1, text=self.m_Receitas)
        self.abas.place(x=0, y=0)
        ####
        self.frameProb = GradientFrame(self.frame_aba1)
        self.frameProb.place(relx=0, rely=0,
                             relwidth=1, relheight=1)

        self.descrCodprod = LabelGlac(self.frame_aba1)
        self.descrCodprod.configure(text='Ano')
        self.descrCodprod.place(x=5, y=15, width=80, height=25)

        self.entry5 = StringVar()
        self.entry5V = {'2020', '2021', '2022', '2023', '2024', '2025'}
        self.entry5V = sorted(self.entry5V)
        self.entry5.set(self.hj.year)
        self.entradaCodReceita = OptionMenu(self.frame_aba1,
            self.entry5, *self.entry5V)
        self.entradaCodReceita.place(x=85, y=15, width=70, height=25)

        self.descrMes = LabelGlac(self.frame_aba1)
        self.descrMes.configure(text='Mês')
        self.descrMes.place(x=5, y=45, width=80, height=25)

        self.entry6 = StringVar()
        self.entry6V = {'1', '2', '3', '4', '5', '6',
                        '7', '8', '9', '10', '11', '12'}
        self.entry6V = sorted(self.entry6V)
        self.entry6.set(self.hj.month)
        self.entradaReceita = OptionMenu(self.frame_aba1, self.entry6, *self.entry6V)
        self.entradaReceita.place(x=85, y=45, width=70, height=25)

        ###  Botao Carrega
        self.botaoAdd = ButtonGlac(self.frame_aba1)
        self.botaoAdd.configure(text=self.m_Carregar,
                                command= self.carrega_receita)
        self.botaoAdd.place(x=25, y=95, width=110, height=25)

        ###  Botao limpa
        self.botaolimpa = ButtonGlac(self.frame_aba1)
        self.botaolimpa.configure(text=self.m_Limpar,
                                  command= self.limpa_receita)
        self.botaolimpa.place(x=25, y=125, width=110, height=25)

        ### Widgets - Listar produtos ###
        self.listaServ = ttk.Treeview(self.frame_aba1, height=10,
            column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Placa)
        self.listaServ.heading("#3", text=self.m_Dia)
        self.listaServ.heading("#4", text=self.m_Mes)
        self.listaServ.heading("#5", text=self.m_Ano)
        self.listaServ.heading("#6", text="")
        self.listaServ.heading("#7", text=self.m_Valor_R)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=70)
        self.listaServ.column("#2", width=140)
        self.listaServ.column("#3", width=60)
        self.listaServ.column("#4", width=60)
        self.listaServ.column("#5", width=75)
        self.listaServ.column("#6", width=30)
        self.listaServ.column("#7", width=100)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.frame_aba1, orient='vertical',
                               command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=736, y=17, width=20, height=222)
        self.listaServ.place(x=200, y=18)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickFinan)

        ### Widgets - Listar produtos ###

        self.listaServ2 = ttk.Treeview(self.frame_aba1, height=1,
                                       column=("col1", "col2", "col3"))
        self.listaServ2.heading("#0", text="")
        self.listaServ2.heading("#1", text=self.m_Ano)
        self.listaServ2.heading("#2", text=self.m_Mes)
        self.listaServ2.heading("#3", text=self.m_Total)

        self.listaServ2.column("#0", width=0)
        self.listaServ2.column("#1", width=60)
        self.listaServ2.column("#2", width=60)
        self.listaServ2.column("#3", width=100)

        self.listaServ2.place(x=500, y=250)
        self.janelaFin.mainloop()
