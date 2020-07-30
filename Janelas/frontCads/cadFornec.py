from funcs.modulos import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.labelStyle import LabelGlac
from Janelas.estiloWidgets.autcomplety import *
from funcs.backCads.backCadForn import *

class Fornecedores(CadForn):
    def cadforn(self):
        self.telaForn()
        self.canvasForn()
    def telaForn(self):
        self.janelaFor = Toplevel()
        self.janelaFor.title(self.m_Fornecedores)
        self.janelaFor.configure(background=self.fundo_do_frame)
        self.janelaFor.geometry("720x290")
        self.janelaFor.resizable(FALSE, FALSE)
        self.janelaFor.transient(self.janela)
        self.janelaFor.focus_force()
        self.janelaFor.grab_set()
    def canvasForn(self):
        # Codigo
        self.descrCod_forn = LabelGlac(self.janelaFor)
        self.descrCod_forn.configure(text=self.m_Codigo + self.m_Pontinhos)
        self.descrCod_forn.place(x=0, y=20)

        self.entradaCod_forn = EntPlaceHold(self.janelaFor, '')
        self.entradaCod_forn.place(x=70, y=20)

        # Fornecedor
        self.descrFornecedor = LabelGlac(self.janelaFor)
        self.descrFornecedor.configure(text=self.m_Fornecedor + self.m_Pontinhos)
        self.descrFornecedor.place(x=1, y=50)

        self.entradaFornecedor = EntPlaceHold(self.janelaFor, '')
        self.entradaFornecedor.place(x=95, y=50, width= 170)

        # Fone
        self.descrFone = LabelGlac(self.janelaFor)
        self.descrFone.configure(text=self.m_Fone + self.m_Pontinhos)
        self.descrFone.place(x=1, y=80)

        self.entradaFone = EntPlaceHold(self.janelaFor, '')
        self.entradaFone.place(x=50, y=80, width= 100)

        #
        self.descrCnpj = LabelGlac(self.janelaFor)
        self.descrCnpj.configure(text=self.m_Cnpj + self.m_Pontinhos)
        self.descrCnpj.place(x=160, y=80)

        self.entradaCnpj = EntPlaceHold(self.janelaFor, '')
        self.entradaCnpj.place(x=205, y=80, width= 130)

        ####
        self.entradaCep = EntPlaceHold(self.janelaFor, '')
        self.entradaCep.place(x=50, y=113, width= 100)

        ####
        self.descrEndereco = LabelGlac(self.janelaFor)
        self.descrEndereco.configure(text=self.m_Endereco)
        self.descrEndereco.place(x=1, y=140, width=80)

        self.entradaEndereco = EntPlaceHold(self.janelaFor, '')
        self.entradaEndereco.place(x=80, y=140, width=250)

        ####
        self.descrMunicipio = LabelGlac(self.janelaFor)
        self.descrMunicipio.configure(text=self.m_Cidade)
        self.descrMunicipio.place(x=1, y=170, width=80)

        self.entradaMunicipio = EntPlaceHold(self.janelaFor, '')
        self.entradaMunicipio.place(x=80, y=170, width=250)

        #
        self.descrDescricao = LabelGlac(self.janelaFor)
        self.descrDescricao.configure(text=self.m_Observacao)
        self.descrDescricao.place(x=0, y=200, width=100)

        self.entradaDescricao = EntPlaceHold(self.janelaFor, '')
        self.entradaDescricao.place(x=100, y=200, width=230)

        self.botaoCarregarForn = ButtonGlac(self.janelaFor)
        self.botaoCarregarForn.configure(text=self.m_Carregar)
        self.botaoCarregarForn.configure(command=self.carrega_fornecedor)
        self.botaoCarregarForn.place(x=120, y=20, width=140)

        self.botaoLimpaForn = ButtonGlac(self.janelaFor)
        self.botaoLimpaForn.configure(text=self.m_Limpar)
        self.botaoLimpaForn.configure(command=self.limpa_fornecedor)
        self.botaoLimpaForn.place(x=270, y=20, width=70)

        self.botaoBuscaForn = ButtonGlac(self.janelaFor)
        self.botaoBuscaForn.configure(text=self.m_Buscar)
        self.botaoBuscaForn.configure(command=self.busca_fornecedor)
        self.botaoBuscaForn.place(x=270, y=50, width=70)

        self.botaoCepForn = ButtonGlac(self.janelaFor)
        self.botaoCepForn.configure(text=self.m_Cep)
        self.botaoCepForn.configure(command=self.cepForn)
        self.botaoCepForn.place(x=0, y=108, width=50, height=25)

        self.botaoNovoForn = ButtonGlac(self.janelaFor)
        self.botaoNovoForn.configure(text=self.m_Novo)
        self.botaoNovoForn.configure(command=self.add_fornec)
        self.botaoNovoForn.place(x=50, y=240, width=90)

        self.botaoAlterarForn = ButtonGlac(self.janelaFor)
        self.botaoAlterarForn.configure(text=self.m_Alterar)
        self.botaoAlterarForn.configure(command=self.mud_fornec)
        self.botaoAlterarForn.place(x=150, y=240, width=90)

        self.botaoApagarFornecedor = ButtonGlac(self.janelaFor)
        self.botaoApagarFornecedor.configure(text=self.m_Apagar)
        self.botaoApagarFornecedor.configure(command=self.del_fornec)
        self.botaoApagarFornecedor.place(x=250, y=240, width=90)

        ### Widgets - Listar veiculos ###
        self.listaServ = ttk.Treeview(self.janelaFor, height=12, column=("col1", "col2", "col3", "col4"))
        self.listaServ.heading("#0", text="")
        self.listaServ.column("#0", width=0)
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.column("#1", width=40)
        self.listaServ.heading("#2", text=self.m_Fornecedores)
        self.listaServ.column("#2", width=120)
        self.listaServ.heading("#3", text=self.m_Fone)
        self.listaServ.column("#3", width=70)
        self.listaServ.heading("#4", text=self.m_Cidade)
        self.listaServ.column("#4", width=100)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janelaFor, orient='vertical',
                               command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=688, y=12, width=20, height=268)
        self.listaServ.place(x=355, y=12)
        self.listaServ.bind("<Double-1>", self.OnDoubleClickForn)

        self.conecta_Glac()
        lista = self.cursor.execute("""
                    SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao 
                    FROM fornecedores ORDER BY fornecedor ASC;
                    """)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
        self.desconecta_Glac()

