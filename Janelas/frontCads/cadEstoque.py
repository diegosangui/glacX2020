from funcs.modulos import *
from funcs.backCads.backCadEstoque import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.labelStyle import LabelGlac
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *
from Janelas.estiloWidgets.buttonStyle import *

class Estoque(CadEstoque):
    def cadest(self):
        janelaEst = Toplevel()
        self.janelaEst = janelaEst
        janelaEst.title(self.m_Estoque)
        janelaEst.configure(background=self.fundo_da_tela)
        janelaEst.geometry("800x405")
        janelaEst.resizable(FALSE, FALSE)
        janelaEst.minsize(width=780, height=420)
        janelaEst.transient(self.janela)
        janelaEst.focus_force()
        janelaEst.grab_set()

        self.conecta_Glac()

        descrNomeServ = LabelGlac(janelaEst)
        descrNomeServ.configure(text=self.m_ControleEstoque,
                                     font=('Comic', '18', 'bold'))
        descrNomeServ.place(x=245, y=1)
        ###  A B A S
        abas = Notebook(janelaEst)
        frame_aba1 = Frame(abas)
        frame_aba2 = Frame(abas)

        frame_aba1.configure(background='lightgray')
        frame_aba2.configure(background='lightgray')

        label1 = Label(frame_aba1)
        label1.pack(padx=385, pady=160)
        label2 = Label(frame_aba2)
        label2.pack(padx=385, pady=160)

        abas.add(frame_aba1, text=self.m_Cadastro + ' ' + self.m_Produtos)
        abas.add(frame_aba2, text=self.m_MovimentaEst)

        abas.place(x=10, y=30)
        #
        frameProb = GradientFrame(frame_aba1)
        frameProb.place(x=10, y=10, width=755, height=320)

        descrCodprod = LabelGlac(frame_aba1)
        descrCodprod.configure(text=self.m_Codigo)
        descrCodprod.place(x=0, y=15, width=80, height=25)

        ## Label produtos
        descrProd = LabelGlac(frame_aba1)
        descrProd.configure(text=self.m_Produtos)
        descrProd.place(x=0, y=45, width=80, height=25)

        ###  Botao Carrega
        botaoAdd = ButtonGlac(frame_aba1)
        botaoAdd.configure(text=self.m_Carregar,
                                command=self.carrega_produtoE)
        botaoAdd.place(x=140, y=15, width=90, height=25)

        ###  Botao limpa
        botaolimpa = ButtonGlac(frame_aba1)
        botaolimpa.configure(text=self.m_Limpar,
                                 command=self.limpa_produtoE)
        botaolimpa.place(x=275, y=15, width=60, height=25)

        ###  Botao busca
        botaoBusca = ButtonGlac(frame_aba1)
        botaoBusca.configure(text=self.m_Buscar,
                                  command=self.busca_produtoE)
        botaoBusca.place(x=275, y=45, width=60, height=25)

        ### Botao Marca Produto
        descrIdMarcaprod = ButtonGlac(frame_aba1)
        descrIdMarcaprod.configure(text=self.m_Marca,
                                        command=self.busca_marcaE)
        descrIdMarcaprod.place(x=0, y=75, width=80, height=25)

        ## Entry codigo
        self.entradaCodprod = Entry(frame_aba1)
        self.entradaCodprod.configure(validate="key",
            validatecommand=self.vcmd6)
        self.entradaCodprod.place(x=80, y=15, width=60, height=25)

        ## Entry descrição Produto
        self.entradaProd = Entry(frame_aba1)
        self.entradaProd.place(x=80, y=45, width=180, height=25)

        self.entradaIdMarcaprod = Entry(frame_aba1, width=6)
        # widget oculto, sem place

        self.entradaMarcaprod = Entry(frame_aba1)
        self.entradaMarcaprod.place(x=80, y=75, width=200, height=25)

        descrIdFornec = ButtonGlac(frame_aba1)
        descrIdFornec.configure(text=self.m_Fornecedor,
                                    command=self.busca_fornecE)
        descrIdFornec.place(x=0, y=105, width=100, height=25)
        self.entradaIdFornec = Entry(frame_aba1, width=6)
        # entradaIdFornec.place(x=85, y=93)

        self.entradaFornec = Entry(frame_aba1)
        self.entradaFornec.place(x=100, y=105, width=200, height=25)

        descrCusto = LabelGlac(frame_aba1)
        descrCusto.configure(text=self.m_Custo_R)
        descrCusto.place(x=0, y=135, width=80, height=25)

        self.entradaCusto = Entry(frame_aba1)
        self.entradaCusto.configure(validate="key",
                                  validatecommand=self.vcmd8float)
        self.entradaCusto.place(x=80, y=135, width=80, height=25)

        descrValor = LabelGlac(frame_aba1)
        descrValor.configure(text=self.m_Valor_R)
        descrValor.place(x=150, y=135, width=80, height=25)

        self.entradaValor = Entry(frame_aba1)
        self.entradaValor.configure(validate="key",
                                  validatecommand=self.vcmd8float)
        self.entradaValor.place(x=220, y=135, width=80, height=25)

        descrDescricao = LabelGlac(frame_aba1)
        descrDescricao.configure(text=self.m_Descricao)
        descrDescricao.place(x=14, y=175)

        self.entradaDescricao = Entry(frame_aba1)
        self.entradaDescricao.place(x=16, y=195, width=300, height=25)

        botaoAdd = ButtonGlac(frame_aba1)
        botaoAdd.configure(text=self.m_Novo,
                                command=self.add_produtoE)
        botaoAdd.place(x=30, y=250, width=80)

        botaoMudServ = ButtonGlac(frame_aba1)
        botaoMudServ.configure(text=self.m_Alterar,
                                    command=self.mud_produtoE)
        botaoMudServ.place(x=130, y=250, width=80)

        botaoDel = ButtonGlac(frame_aba1)
        botaoDel.configure(text=self.m_Apagar,
                                command=self.del_produtoE)
        botaoDel.place(x=230, y=250, width=80)

        ### Widgets - Listar produtos ###
        self.listaServ = ttk.Treeview(frame_aba1, height=10,
            column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Produtos)
        self.listaServ.heading("#3", text="")
        self.listaServ.heading("#4", text=self.m_Custo_R)
        self.listaServ.heading("#5", text="")
        self.listaServ.heading("#6", text=self.m_Valor_R)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=60)
        self.listaServ.column("#2", width=140)
        self.listaServ.column("#3", width=25)
        self.listaServ.column("#4", width=65)
        self.listaServ.column("#5", width=25)
        self.listaServ.column("#6", width=85)

        # Cria barra de rolagem
        self.barra = Scrollbar(frame_aba1, orient='vertical',
                               command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=740, y=15, width=15, height=300)

        lista = self.cursor.execute("""
            SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
            WHERE sp = "P" ORDER BY servprod ASC ;
                            """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.place(x=340, y=15, height=300)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickE)

        #####################################################################
        #### ABA 2
        #############################
        ### Cabeçalho dos itens_orc 1 A 10 - Aba 2
        frameItens = GradientFrame(frame_aba2)
        frameItens.place(x=10, y=8, width=760, height=316)

        ### Produto
        produto_aba2label = LabelGlac(frame_aba2)
        produto_aba2label.configure(text=self.m_Produtos)
        produto_aba2label.place(x=20, y=20, width=80, height=25)

        self.codproduto2 = Entry(frame_aba2)

        self.produto_aba2 = Entry(frame_aba2)
        self.produto_aba2.place(x=100, y=20, width=400, height=25)

        #### Entrada
        quant_aba2label = LabelGlac(frame_aba2)
        quant_aba2label.configure(text=self.m_Entrada)
        quant_aba2label.place(x=20, y=50, width=80, height=25)

        self.quant_aba2 = Entry(frame_aba2)
        self.quant_aba2.configure(validate="key",
                                validatecommand=self.vcmd8float)
        self.quant_aba2.place(x=100, y=50, width=100, height=25)
        self.quant_aba2.insert(END, 0)

        #### Saida
        saida_aba2label = LabelGlac(frame_aba2)
        saida_aba2label.configure(text=self.m_Saida)
        saida_aba2label.place(x=20, y=80, width=80, height=25)

        self.saida_aba2 = Entry(frame_aba2)
        self.saida_aba2.configure(validate="key",
                                validatecommand=self.vcmd8float)
        self.saida_aba2.place(x=100, y=80, width=100, height=25)
        self.saida_aba2.insert(0, 0)

        #### Custo
        custo_aba2label = LabelGlac(frame_aba2)
        custo_aba2label.configure(text=self.m_Custo_R)
        custo_aba2label.place(x=20, y=110, width=80, height=25)

        self.custo_aba2 = Entry(frame_aba2)
        self.custo_aba2.configure(validate="key", validatecommand=self.vcmd8float)
        self.custo_aba2.place(x=100, y=110, width=100, height=25)

        #### Data
        data_aba2label = LabelGlac(frame_aba2)
        data_aba2label.configure(
            text=self.m_Data)
        data_aba2label.place(x=20, y=140, width=80, height=25)

        self.dia_aba2 = Entry(frame_aba2)
        self.dia_aba2.configure(validate="key", validatecommand=self.vcmd2)
        self.dia_aba2.place(x=100, y=140, width=25, height=25)
        self.dia_aba2.insert(END, self.hj.day)

        self.mes_aba2 = StringVar()
        self.mes_aba2V = {'1', '2', '3', '4', '5', '6',
                        '7', '8', '9', '10', '11', '12'}
        self.mes_aba2V = sorted(self.mes_aba2V)
        self.mes_aba2.set(self.hj.month)
        self.entradaMes = OptionMenu(frame_aba2, self.mes_aba2, *self.mes_aba2V)
        self.entradaMes.place(x=125, y=140, width=50, height=25)

        self.ano_aba2 = StringVar()
        self.ano_aba2V = {'2020', '2021', '2022', '2023', '2024', '2025'}
        self.ano_aba2V = sorted(self.ano_aba2V)
        self.ano_aba2.set(self.hj.year)
        self.entradaAno = OptionMenu(frame_aba2,
                                    self.ano_aba2, *self.ano_aba2V)
        self.entradaAno.place(x=150, y=140, width=70, height=25)

        #### Lote
        lote_aba2label = LabelGlac(frame_aba2)
        lote_aba2label.configure(text=self.m_Lote)
        lote_aba2label.place(x=20, y=170, width=80, height=25)

        self.lote_aba2 = EntPlaceHold(frame_aba2, '')
        self.lote_aba2.place(x=100, y=170, width=100, height=25)

        #### Validade
        valid_aba2label = LabelGlac(frame_aba2)
        valid_aba2label.configure(text=self.m_Validade)
        valid_aba2label.place(x=20, y=200, width=80, height=25)

        self.diaV_aba2 = Entry(frame_aba2)
        self.diaV_aba2.configure(validate="key", validatecommand=self.vcmd2)
        self.diaV_aba2.place(x=100, y=200, width=25, height=25)
        self.diaV_aba2.insert(END, self.hj.day)

        self.mesV_aba2 = StringVar()
        self.mesV_aba2V = {'1', '2', '3', '4', '5', '6',
                          '7', '8', '9', '10', '11', '12'}
        self.mesV_aba2V = sorted(self.mes_aba2V)
        self.mesV_aba2.set(self.hj.month)
        self.entradaMesV = OptionMenu(frame_aba2, self.mesV_aba2, *self.mesV_aba2V)
        self.entradaMesV.place(x=125, y=200, width=50, height=25)

        self.anoV_aba2 = StringVar()
        self.anoV_aba2V = {'2020', '2021', '2022', '2023', '2024', '2025'}
        self.anoV_aba2V = sorted(self.ano_aba2V)
        self.anoV_aba2.set(self.hj.year)
        self.entradaAno = OptionMenu(frame_aba2,
                                     self.anoV_aba2, *self.anoV_aba2V)
        self.entradaAno.place(x=150, y=200, width=70, height=25)

        darEntrada = ButtonGlac(frame_aba2)
        darEntrada.configure(text=self.m_InserirRegistro, command=self.add_movE)
        darEntrada.place(x=40, y=260, width=140, height=25)

        quantestlabel = LabelGlac(frame_aba2)
        quantestlabel.configure(text=self.m_Quant + ' ' + self.m_Estoque)
        quantestlabel.place(x=430, y=290, width=150, height=25)

        self.quantest = Entry(frame_aba2)
        self.quantest.place(x=580, y=290, width=100, height=25)

        ### Widgets - Listar produtos ###
        self.listaMov = ttk.Treeview(frame_aba2, height=10,
            column=("col1", "col2", "col3", "col4", "col5", "col6",
                    "col7", "col8", "col9", "col10", "col11"))
        self.listaMov.heading("#0", text="")
        self.listaMov.heading("#1", text=self.m_Lote)
        self.listaMov.heading("#2", text="Entr")
        self.listaMov.heading("#3", text="Said")
        self.listaMov.heading("#4", text="Custo")
        self.listaMov.heading("#5", text="D")
        self.listaMov.heading("#6", text="M")
        self.listaMov.heading("#7", text=self.m_Data)
        self.listaMov.heading("#8", text="Forn")
        self.listaMov.heading("#9", text="D")
        self.listaMov.heading("#10", text="M")
        self.listaMov.heading("#11", text=self.m_Validade)

        self.listaMov.column("#0", width=1)
        self.listaMov.column("#1", width=60)
        self.listaMov.column("#2", width=50)
        self.listaMov.column("#3", width=50)
        self.listaMov.column("#4", width=60)
        self.listaMov.column("#5", width=25)
        self.listaMov.column("#6", width=25)
        self.listaMov.column("#7", width=45)
        self.listaMov.column("#8", width=80)
        self.listaMov.column("#9", width=25)
        self.listaMov.column("#10", width=25)
        self.listaMov.column("#11", width=65)

        # Cria barra de rolagem
        self.barraMov = Scrollbar(frame_aba2, orient='vertical',
                                  command=self.listaMov.yview)

        # Adiciona barra de rolagem
        self.listaMov.configure(yscroll=self.barraMov.set)
        self.barraMov.place(x=742, y=50, width=20, height=220)

        # Adiciona barra de rolagem
        self.listaMov.place(x=235, y=50)
        self.listaMov.bind("<Double-1>", self.OnDoubleClickE)

        self.desconecta_Glac()
        janelaEst.mainloop()
    def busca_fornecE(self):
        self.conecta_Glac()
        ### Widgets - Listar tecnicos ###

        self.entradaFornec.insert(END, '%')
        veicAuto = self.entradaFornec.get()

        self.listatec = Toplevel()
        self.listatec.title("Fornecedores - GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("310x240")
        self.listatec.resizable(TRUE, TRUE)
        self.listatec.transient(self.janelaEst)
        self.listatec.focus_force()
        self.listatec.grab_set()
        ##########
        self.listatec1 = ttk.Treeview(self.listatec, height=10,
                                      column=("col1", "col2"))
        self.listatec1.heading("#0", text="")
        self.listatec1.heading("#1", text="Cod")
        self.listatec1.heading("#2", text="Fornecedor")

        self.listatec1.column("#0", width=0)
        self.listatec1.column("#1", width=60)
        self.listatec1.column("#2", width=220)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.listatec, orient='vertical',
                               command=self.listatec1.yview)

        # Adiciona barra de rolagem
        self.listatec1.configure(yscroll=self.barra.set)
        self.barra.place(x=280, y=12, width=25, height=220)

        self.listatec1.place(x=5, y=5)

        lista = self.cursor.execute("""SELECT cod_forn, fornecedor 
            FROM fornecedores ORDER BY fornecedor ASC""")

        rows = self.cursor.fetchall()
        for row in rows:
            self.listatec1.insert("", END, values=row)

            # Binding da listbox
        self.listatec1.bind('<Double-1>', self.add_autobind)

        self.entradaFornec.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.desconecta_Glac()
    def busca_marcaE(self):
        self.conecta_Glac()
        ### Widgets - Listar tecnicos ###

        self.entradaMarcaprod.insert(END, '%')

        veicAuto = self.entradaMarcaprod.get()

        self.listatec = Toplevel()
        self.listatec.title("Marcas - GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("310x240")
        self.listatec.resizable(TRUE, TRUE)
        self.listatec.transient(self.janelaEst)
        self.listatec.focus_force()
        self.listatec.grab_set()

        ##########
        self.listatec1 = ttk.Treeview(self.listatec, height=10,
                                      column=("col1", "col2"))
        self.listatec1.heading("#0", text="")
        self.listatec1.heading("#1", text="Cod")
        self.listatec1.heading("#2", text="Marca")

        self.listatec1.column("#0", width=0)
        self.listatec1.column("#1", width=60)
        self.listatec1.column("#2", width=220)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.listatec, orient='vertical',
                               command=self.listatec1.yview)

        # Adiciona barra de rolagem
        self.listatec1.configure(yscroll=self.barra.set)
        self.barra.place(x=280, y=6, width=30, height=225)

        self.listatec1.place(x=5, y=5)

        lista = self.cursor.execute("""
            SELECT cod_marca, marca FROM marcaprod ORDER BY marca ASC""")

        rows = self.cursor.fetchall()
        for row in rows:
            self.listatec1.insert("", END, values=row)

            # Binding da listbox
        self.listatec1.bind('<Double-1>', self.add_autobind2)

        self.entradaMarcaprod.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.desconecta_Glac()
