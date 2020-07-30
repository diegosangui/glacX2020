from funcs.modulos import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.labelStyle import LabelGlac
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *

class Aba2:
    def aba2(self):
        # Cabeçalho dos itens_orc 1 A 10 - Aba 2
        self.frameItens = GradientFrame(self.frame_aba2)
        self.frameItens.place(relx=0.002, rely=0.01,
                              relwidth=0.99, relheight=0.99)
        # Label codigo
        self.descrCodI = LabelGlac(self.frame_aba2)
        self.descrCodI.configure(bg=self.bg_button, fg=self.fg_label,
            text='Código / Item')
        self.descrCodI.place(relx=0.56, rely=0.02,
                             relwidth=0.12, relheight=0.09)
        # Label Servicos Peças
        self.descrCol2 = LabelGlac(self.frame_aba2)
        self.descrCol2.configure(text = 'Serviços / Produtos', justify='center'
            ,fg=self.bg_label, bg=self.fg_label)
        self.descrCol2.place(relx=0.01, rely=0.02,
                             relwidth=0.55, relheight=0.09)

        # Label Valor
        self.descrCol3 = Label(self.frame_aba2, text=self.m_ValorUnit,
            bg=self.bg_label, fg=self.fg_label, font=('Verdana', '10', 'bold'));
        self.descrCol3.place(relx=0.69, rely=0.02,
                             relwidth=0.09, relheight=0.09)

        # Quantidade
        self.descrQuant = ButtonGlac(self.frame_aba2)
        self.descrQuant.configure(text=self.m_Quant, bg=self.fg_label,
            fg=self.bg_label, command=self.altera_itens_orc_quant2,
            font=('Verdana', '10', 'bold'))
        self.descrQuant.place(relx=0.78, rely=0.02,
                              relwidth=0.05, relheight=0.09)

        ###     Total Item
        self.descrTotalItem = Label(self.frame_aba2, text=self.m_Total + ' ' + self.m_Item, bg=self.bg_label,
                                    fg=self.fg_label, font=('Verdana', '10', 'bold'))
        self.descrTotalItem.place(relx=0.83, rely=0.02,
                                  relwidth=0.1, relheight=0.09)

        ###############################
        ### Widgets - Listar item 1 ###
        self.listaCol2a = AutocompleteEntrySP(self.frame_aba2)
        self.listaCol2a.place(relx=0.01, rely=0.11,
                              relwidth=0.5, relheight=0.1)

        ### Codigo do Item
        self.codServ1 = Entry(self.frame_aba2, validate="key", width=6, bd=1,
            justify='center', fg=self.fg_entry, bg=self.bg_entry,
            validatecommand=self.vcmd6, font=('Verdana', '8', 'bold'))
        self.codServ1.place(relx=0.56, rely=0.11,
                            relwidth=0.06, relheight=0.1)

        self.btSeta = self.btSeta.subsample(4,5)
        self.botaoAddServicos1 = Button(self.frame_aba2,
            image= self.btSeta,command=self.add_servico1)
        self.botaoAddServicos1.place(relx=0.63, rely=0.11, width=30, height=25)

        #### Botao Busca Item
        self.botaoBuscaSP1 = Button(self.frame_aba2, bd=0, bg=self.bg_label,
            image=self.tecnicoBt, command=self.busca_servico1)
        self.botaoBuscaSP1.place(relx=0.51, rely=0.11,
                                 width=38, height=31)
        #### Coluna Quantidade
        self.listaCol3a = EntPlaceHold(self.frame_aba2, '')
        self.listaCol3a.config(validate="key",
                               validatecommand=self.vcmd4float,
                                bd=1, justify='center',
                               font=('Verdana', '8', 'bold'))
        self.listaCol3a.place(relx=0.78, rely=0.11,
                              relwidth=0.05, relheight=0.1)
        #### Coluna Valor
        self.listaCol4a = EntPlaceHold(self.frame_aba2, '')
        self.listaCol4a.config(validate="key", justify='right')
        self.listaCol4a.place(relx=0.69, rely=0.11,
                              relwidth=0.09, relheight=0.1)
        ###### Coluna Total Unitario
        self.listaCol5a = Entry(self.frame_aba2)
        self.listaCol5a.config(validate="key")
        self.listaCol5a.place(relx=0.83, rely=0.11,
                              relwidth=0.1, relheight=0.1)
        ###### ADD
        self.add = self.add.subsample(4,5)
        self.botaoAddServicos2 = Button(self.frame_aba2, bd=1, bg=self.bg_label,
            image=self.add, command=self.add_itens_orc)
        self.botaoAddServicos2.place(relx=0.931, rely=0.11,
                                     width=30, height=25)
        # treeview #
        self.barraServProd = Scrollbar(self.frame_aba2, orient='vertical',
                                       command=self.OnVsb_Orc2)

        self.listaServProd = ttk.Treeview(self.frame_aba2, height=10,
            yscrollcommand=self.barraServProd.set, column=("col1", "col2",
            "col3", "col4", "col5", "col6"))

        self.listaServProd.heading("#0", text="")
        self.listaServProd.heading("#1", text=self.m_Item)
        self.listaServProd.heading("#2", text=self.m_Serviços)
        self.listaServProd.heading("#3", text=self.m_Codigo)
        self.listaServProd.heading("#4", text=self.m_Valor)
        self.listaServProd.heading("#5", text=self.m_Quant)
        self.listaServProd.heading("#6", text=self.m_Valor + ' ' + self.m_Total)

        self.listaServProd.column("#0", width=1)
        self.listaServProd.column("#1", width=10)
        self.listaServProd.column("#2", width=450)
        self.listaServProd.column("#3", width=45)
        self.listaServProd.column("#4", width=60)
        self.listaServProd.column("#5", width=45)
        self.listaServProd.column("#6", width=60)

        self.listaServProd.place(relx=-0.031, rely=0.24,
                                 relwidth=0.98, relheight=0.72)

        self.listaServProd.configure(yscroll=self.barraServProd.set)
        self.barraServProd.place(relx=0.948, rely=0.24,
                                 relwidth=0.02, relheight=0.72)
        self.listaServProd.bind('<Double-1>', self.altera_itens_orc)
        self.listaServProd.bind('<Return>', self.altera_itens_orc)
        self.listaServProd.bind('<Delete>', self.altera_itens_orc_deletabt2)