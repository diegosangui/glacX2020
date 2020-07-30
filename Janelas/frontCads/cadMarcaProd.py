from funcs.modulos import *
from funcs.backCads.backCadMarcaProd import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.labelStyle import LabelGlac
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *

class MarcaProdutos(CadMarcaProd):
    def cadmarcaprod(self):
        self.janelaM = Toplevel()
        self.janelaM.title(self.m_Marca + ' ' + self.m_Produtos)
        self.janelaM.configure(background=self.fundo_do_frame)
        self.janelaM.geometry("870x200")
        self.janelaM.resizable(FALSE, FALSE)
        self.janelaM.transient(self.janela)
        self.janelaM.focus_force()
        self.janelaM.grab_set()

        self.descrCod = LabelGlac(self.janelaM)
        self.descrCod.configure(text= self.m_Codigo)
        self.descrCod.place(x=5, y=20, width=80, height=25)

        self.entradaCod = EntPlaceHold(self.janelaM, '')
        self.entradaCod.place(x=85, y=20, width=50, height=25)

        ###  Botao Carrega marca
        self.botaoAdd = ButtonGlac(self.janelaM)
        self.botaoAdd.configure(text= self.m_Carregar,
                                command=self.carrega_marca_prod)
        self.botaoAdd.place(x=145, y=20, width=130, height=25)

        ###  Botao limpa automovel
        self.botaolimpa = ButtonGlac(self.janelaM)
        self.botaolimpa.configure(text= self.m_Limpar,
                                  command=self.limpa_marca_prod)
        self.botaolimpa.place(x=280, y=20, width=70, height=25)

        self.descrMarca = LabelGlac(self.janelaM)
        self.descrMarca.configure(text= self.m_Marca)
        self.descrMarca.place(x=5, y=50, width=80, height=25)

        self.entradaMarca = EntPlaceHold(self.janelaM, '')
        self.entradaMarca.place(x=85, y=50, width=200, height=25)

        ###  Botao busca automovel
        self.botaobusca = ButtonGlac(self.janelaM)
        self.botaobusca.configure(text= self.m_Buscar,
                                  command=self.busca_marca_prod)
        self.botaobusca.place(x=285, y=50, width=70, height=25)

        self.descrDescricao = LabelGlac(self.janelaM)
        self.descrDescricao.configure(text= self.m_Descricao)
        self.descrDescricao.place(x=5, y=90, width=80, height=25)

        self.entradaDescricao = EntPlaceHold(self.janelaM, '')
        self.entradaDescricao.place(x=85, y=90, width=250, height=25)

        # Botao adicionar
        self.botaoAdd = ButtonGlac(self.janelaM)
        self.botaoAdd.configure(text= self.m_Novo,
                                command=self.add_marca_prod)
        self.botaoAdd.place(x=30, y=150, width=85, height=25)

        # botao mudar
        self.botaoMud = ButtonGlac(self.janelaM)
        self.botaoMud.configure(text= self.m_Alterar,
                                command=self.mud_marca_prod)
        self.botaoMud.place(x=130, y=150, width=85, height=25)

        # botao deletar
        self.botaoDel = ButtonGlac(self.janelaM)
        self.botaoDel.configure(text=" Apagar ",
                                command=self.del_marca_prod)
        self.botaoDel.place(x=230, y=150, width=85, height=25)

        ### Widgets - Listar produtos ###
        self.listaServ = ttk.Treeview(self.janelaM, height=7,
                                      column=("col1", "col2", "col3"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text= self.m_Codigo)
        self.listaServ.heading("#2", text= self.m_Marca)
        self.listaServ.heading("#3", text= self.m_Descricao)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=65)
        self.listaServ.column("#2", width=200)
        self.listaServ.column("#3", width=220)
        self.listaServ.place(x=360, y=20)

        self.conecta_Glac()

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janelaM, orient='vertical', command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=845, y=20, width=20, height=160)

        lista = self.cursor.execute("""
            SELECT cod_marca, marca, descricao FROM marcaprod ORDER BY marca ASC ;
            """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickMarc)
        self.desconecta_Glac()

        self.janelaM.mainloop()
