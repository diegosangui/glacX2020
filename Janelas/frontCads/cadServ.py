from funcs.modulos import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.labelStyle import *
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *
from Janelas.estiloWidgets.buttonStyle import *
from funcs.backCads.backCadServ import *

class Servicos(CadServ):
    def cadserv(self):
        self.janelaServ = Toplevel()
        self.janelaServ.title(self.m_Serviços)
        self.janelaServ.configure(background= 'lightgray')
        self.janelaServ.geometry("1000x390")
        self.janelaServ.resizable(FALSE, FALSE)
        self.janelaServ.transient(self.janela)
        self.janelaServ.focus_force()
        self.janelaServ.grab_set()

        self.descrCod = LabelGlac(self.janelaServ)
        self.descrCod.configure(text= self.m_Codigo + self.m_Pontinhos)
        self.descrCod.place(x=6, y=15, width=80, height=25)

        self.entradaCod = EntPlaceHold(self.janelaServ, '')
        self.entradaCod.place(x=80, y=15, width=40, height=25)

        ###  Botao Carrega servico
        self.botaoAdd = ButtonGlac(self.janelaServ)
        self.botaoAdd.configure(text= self.m_Carregar,
                                command=self.carrega_servicoS)
        self.botaoAdd.place(x=145, y=15, width=130, height=25)

        ###  Botao limpa servico
        self.botaolimpa = ButtonGlac(self.janelaServ)
        self.botaolimpa.configure(text= self.m_Limpar,
                                  command=self.limpa_servicoS)
        self.botaolimpa.place(x=280, y=15, width=70, height=25)

        self.descrServ = LabelGlac(self.janelaServ)
        self.descrServ.configure(text= self.m_Serviços)
        self.descrServ.place(x=6, y=60, width=80, height=25)

        self.entradaServ = EntPlaceHold(self.janelaServ, '')
        self.entradaServ.place(x=80, y=60, width=350, height=25)

        ###  Botao busca SERVICO
        self.botaolimpa = ButtonGlac(self.janelaServ)
        self.botaolimpa.configure(text= self.m_Buscar,
                                  command=self.busca_servicoS)
        self.botaolimpa.place(x=360, y=15, width=70, height=25)

        self.descrHor = LabelGlac(self.janelaServ)
        self.descrHor.configure(text= self.m_Horas)
        self.descrHor.place(x=6, y=110, width=80, height=25)

        self.entradaHor = EntPlaceHold(self.janelaServ,'')
        self.entradaHor.place(x=80, y=110, width=40, height=25)

        self.descrCustohora = LabelGlac(self.janelaServ)
        self.descrCustohora.configure(text= self.m_Custo_R)
        self.descrCustohora.place(x=140, y=110, width=70, height=25)

        self.entradaCustohora = EntPlaceHold(self.janelaServ, '')
        self.entradaCustohora.place(x=210, y=110,  width=40, height=25)

        self.descrValorhora = LabelGlac(self.janelaServ)
        self.descrValorhora.configure(text= self.m_Valor_R)
        self.descrValorhora.place(x=270, y=110, width=70, height=25)

        self.entradaValorhora = EntPlaceHold(self.janelaServ, '')
        self.entradaValorhora.place(x=335, y=110, width=40, height=25)

        self.descrTipoServ = LabelGlac(self.janelaServ)
        self.descrTipoServ.configure(text= self.m_Tipo)
        self.descrTipoServ.place(x=445, y=15, width=80, height=25)

        self.entradaTipoServ = EntPlaceHold(self.janelaServ, '')
        self.entradaTipoServ.place(x=525, y=15, width=200, height=25)

        self.descrSistemaServ = LabelGlac(self.janelaServ)
        self.descrSistemaServ.configure(text= self.m_Sistema)
        self.descrSistemaServ.place(x=445, y=45, width=80, height=25)

        self.entradaSistemaServ = EntPlaceHold(self.janelaServ, '')
        self.entradaSistemaServ.place(x=525, y=45, width=200, height=25)

        self.descrDescricao = LabelGlac(self.janelaServ)
        self.descrDescricao.configure(text= self.m_Marca)
        self.descrDescricao.place(x=445, y=75, width=80, height=25)

        self.entradaDescricao = EntPlaceHold(self.janelaServ, '')
        self.entradaDescricao.place(x=525, y=75, width=200, height=25)

        self.descrVeic = ButtonGlac(self.janelaServ)
        self.descrVeic.configure(text= self.m_Veiculo,
                                 command=self.busca_serv_veicS)
        self.descrVeic.place(x=445, y=105, width=80, height=25)

        self.entradaVeic = EntPlaceHold(self.janelaServ, '')
        self.entradaVeic.place(x=525, y=105, width=200, height=25)

        self.botaoAdd = ButtonGlac(self.janelaServ)
        self.botaoAdd.configure(text= self.m_Novo,
                                command=self.add_servS)
        self.botaoAdd.place(x=800, y=20, width=90, height=25)

        self.botaoMudServ = ButtonGlac(self.janelaServ)
        self.botaoMudServ.configure(text= self.m_Alterar,
                                    command=self.mud_servS)
        self.botaoMudServ.place(x=800, y=50, width=90, height=25)

        self.botaoDel = ButtonGlac(self.janelaServ)
        self.botaoDel.configure(text= self.m_Apagar,
                                command=self.del_servS)
        self.botaoDel.place(x=800, y=80, width=90, height=25)

        ### Widgets - Listar veiculos ###
        self.listaServ = ttk.Treeview(self.janelaServ, height=10,
            column=("col1", "col2", "col3", "col4", "col5", "col6",
                    "col7", "col8", "col9"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text= self.m_Codigo)
        self.listaServ.heading("#2", text= self.m_Serviços)
        self.listaServ.heading("#3", text= self.m_Horas)
        self.listaServ.heading("#4", text= self.m_Custo_R)
        self.listaServ.heading("#5", text= self.m_Valor)
        self.listaServ.heading("#6", text= self.m_Marca)
        self.listaServ.heading("#7", text= self.m_Veiculo)
        self.listaServ.heading("#8", text= self.m_Tipo)
        self.listaServ.heading("#9", text= self.m_Sistema)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=60)
        self.listaServ.column("#2", width=230)
        self.listaServ.column("#3", width=45)
        self.listaServ.column("#4", width=57)
        self.listaServ.column("#5", width=55)
        self.listaServ.column("#6", width=100)
        self.listaServ.column("#7", width=145)
        self.listaServ.column("#8", width=110)
        self.listaServ.column("#9", width=145)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janelaServ, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=960, y=150, width=20, height=230)

        self.conecta_Glac()

        lista = self.cursor.execute("""
            SELECT cod_sp, servprod, hor, custo , valor, descricao, id_marcaprod, tiposerv, sistemaserv FROM servprod  WHERE sp = "s" ORDER BY servprod ASC;
            """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.place(x=15, y=150)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickS)

        self.desconecta_Glac()

        self.janelaServ.mainloop()
