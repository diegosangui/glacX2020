from funcs.modulos import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.labelStyle import LabelGlac
from Janelas.estiloWidgets.autcomplety import *
from funcs.backCads.backCadProduto import *

class Produtos(CadProdutos):
    def cadprod(self):
        # Montagem da Janela
        self.janelaProd = Toplevel()
        self.janelaProd.configure(background= self.fundo_do_frame)
        self.janelaProd.title(self.m_Produtos)
        self.janelaProd.geometry("882x250")
        self.janelaProd.resizable(FALSE, FALSE)
        self.janelaProd.transient(self.janela)
        self.janelaProd.focus_force()
        self.janelaProd.grab_set()

        # Criação dos widgets

        ########################################################
        # Código do Produto
        #Label
        self.descrCodprod = LabelGlac(self.janelaProd)
        self.descrCodprod.configure(text= self.m_Codigo)
        self.descrCodprod.place(x=2, y=5, width=80, height=25)
        # Entry
        self.entradaCodprod = EntPlaceHold(self.janelaProd, '')
        self.entradaCodprod.place(x=75, y=5, width=60, height=25)
        ##########################################################
        # Descrição do produto
        #Label
        self.descrProd = LabelGlac(self.janelaProd)
        self.descrProd.configure(text=self.m_Produtos)
        self.descrProd.place(x=2, y=33, width=80, height=25)
        # Entry
        self.entradaProd = EntPlaceHold(self.janelaProd, '')
        self.entradaProd.place(x=80, y=33, width=200, height=25)
        #########################################################
        # Botao Carrega
        self.botaoAdd = ButtonGlac(self.janelaProd)
        self.botaoAdd.configure(text= self.m_Carregar,
            command= self.carrega_produtoP)
        self.botaoAdd.place(x=150, y=2, width=115)
        ########################################################
        # Botao limpa
        self.botaolimpa = ButtonGlac(self.janelaProd)
        self.botaolimpa.configure(command=self.limpa_produtoP,
                                  text= self.m_Limpar)
        self.botaolimpa.place(x=275, y=2, width=70, height=25)

        ########################################################
        ###  Botao busca automovel
        self.botaolimpa = ButtonGlac(self.janelaProd)
        self.botaolimpa.configure(command=self.busca_produtoP,
                                  text= self.m_Buscar)
        self.botaolimpa.place(x=275, y=30, width=70, height=25)
        #######################################################
        # Botão Marca do Produto
        self.descrIdMarcaprod = ButtonGlac(self.janelaProd)
        self.descrIdMarcaprod.configure(text= self.m_Marca,
                                        command=self.busca_marcaP)
        self.descrIdMarcaprod.place(x=2, y=62, width=100, height=25)
        # Entry oculta
        self.entradaIdMarcaprod = Entry(self.janelaProd, width=6)

        self.entradaMarcaprod = EntPlaceHold(self.janelaProd, '')
        self.entradaMarcaprod.place(x=105, y=62, width=250, height=25)

        self.descrIdFornec = ButtonGlac(self.janelaProd)
        self.descrIdFornec.configure(text= self.m_Fornecedor,
                                     command=self.busca_fornecP)
        self.descrIdFornec.place(x=1, y=92, width=100, height=25)

        self.entradaIdFornec = Entry(self.janelaProd, width=6)

        self.entradaFornec = EntPlaceHold(self.janelaProd, '')
        self.entradaFornec.place(x=105, y=93, width=250, height=25)

        self.descrCusto = LabelGlac(self.janelaProd)
        self.descrCusto.configure(text= self.m_Custo_R)
        self.descrCusto.place(x=2, y=122, width=80, height=25)

        self.entradaCusto = EntPlaceHold(self.janelaProd, '')
        self.entradaCusto.configure(validate="key",
            validatecommand=self.vcmd8float)
        self.entradaCusto.place(x=83, y=122, width=80, height=25)

        self.descrValor = LabelGlac(self.janelaProd)
        self.descrValor.configure(text= self.m_Valor_R)
        self.descrValor.place(x=170, y=122, width=80, height=25)

        self.entradaValor = EntPlaceHold(self.janelaProd, '')
        self.entradaValor.configure(validate="key",
                                    validatecommand=self.vcmd8float)
        self.entradaValor.place(x=250, y=123, width=80, height=25)

        self.descrDescricao = LabelGlac(self.janelaProd)
        self.descrDescricao.configure(text= self.m_Descricao)
        self.descrDescricao.place(x=2, y=150, width=80, height=25)

        self.entradaDescricao = EntPlaceHold(self.janelaProd, '')
        self.entradaDescricao.place(x=83, y=153, width=250, height=25)

        self.botaoAdd = ButtonGlac(self.janelaProd)
        self.botaoAdd.configure(text= self.m_Novo,
                                command=self.add_produtoP)
        self.botaoAdd.place(x=50, y=190, width=80, height=35)

        self.botaoMudServ = ButtonGlac(self.janelaProd)
        self.botaoMudServ.configure(text= self.m_Alterar,
                                    command=self.mud_produtoP)
        self.botaoMudServ.place(x=150, y=190, width=80, height=35)

        self.botaoDel = ButtonGlac(self.janelaProd)
        self.botaoDel.configure(text= self.m_Apagar,
            command=self.del_produtoP)
        self.botaoDel.place(x=250, y=190, width=80, height=35)

        ### Widgets - Listar produtos ###
        self.listaServ = ttk.Treeview(self.janelaProd,
            height=10, column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaServ.heading("#0", text="")
        self.listaServ.column("#0", width=0)
        self.listaServ.heading("#1", text= self.m_Codigo)
        self.listaServ.column("#1", width=60)
        self.listaServ.heading("#2", text= self.m_Produtos)
        self.listaServ.column("#2", width=220)
        self.listaServ.heading("#3", text="")
        self.listaServ.column("#3", width=25)
        self.listaServ.heading("#4", text= self.m_Custo_R)
        self.listaServ.column("#4", width=70)
        self.listaServ.heading("#5", text="")
        self.listaServ.column("#5", width=25)
        self.listaServ.heading("#6", text= self.m_Valor_R)
        self.listaServ.column("#6", width=80)

        self.conecta_Glac()

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janelaProd, orient='vertical',
                               command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=845, y=5, width=20, height=230)

        lista = self.cursor.execute("""
            SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
      	    WHERE sp = "P" ORDER BY servprod ASC ;
            """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.place(x=360, y=5)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickP)

        self.desconecta_Glac()

        self.janelaProd.mainloop()
