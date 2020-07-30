from funcs.modulos import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.labelStyle import LabelGlac
from Janelas.estiloWidgets.autcomplety import *
from funcs.backCads.backCadTec import *

class Tecnicos(CadTec):
    def cadtec(self):
        self.janelaTec = Toplevel()
        self.janelaTec.title(self.m_Tecnico)
        self.janelaTec.configure(background=self.fundo_do_frame)
        self.janelaTec.geometry("650x210")
        self.janelaTec.transient(self.janela)
        self.janelaTec.focus_force()
        self.janelaTec.grab_set()

        self.janelaTec.resizable(FALSE, FALSE)

        ###  Botao Novo Cliente
        self.botaoAdd = ButtonGlac(self.janelaTec)
        self.botaoAdd.configure(text=self.m_Novo)
        self.botaoAdd.configure(command=self.add_servT)
        self.botaoAdd.place(x=30, y=140, width=80, height=35)

        ### Botao Altera dados do Cliente
        self.botaoMud = ButtonGlac(self.janelaTec)
        self.botaoMud.configure(text=self.m_Alterar)
        self.botaoMud.configure(command=self.mud_servT)
        self.botaoMud.place(x=130, y=140, width=80, height=35)

        ### Botao deletar dados do Cliente
        self.botaoDel = ButtonGlac(self.janelaTec)
        self.botaoDel.configure(text=self.m_Apagar)
        self.botaoDel.configure(command=self.del_servT)
        self.botaoDel.place(x=230, y=140, width=80, height=35)

        ##  Botao limpa
        self.botaolimpa = ButtonGlac(self.janelaTec)
        self.botaolimpa.configure(text=self.m_Limpar,
                                  command=self.limpa_servicoT)
        self.botaolimpa.place(x=270, y=50, width=70, height=25)

        ###  Botao busca Cabeça
        self.botaobusca = ButtonGlac(self.janelaTec)
        self.botaobusca.configure(bitmap='questhead',
                                  command=self.busca_servicoT)
        self.botaobusca.place(x=290, y=80, width=30, height=30)

        ###  Botao busca Carregar
        self.botaoCarregar = ButtonGlac(self.janelaTec)
        self.botaoCarregar.configure(text=self.m_Carregar,
                                     command=self.carrega_servicoT)
        self.botaoCarregar.place(x=135, y=50, width=130, height=25)


        self.descrCod = LabelGlac(self.janelaTec)
        self.descrCod.configure(text=self.m_Codigo)
        self.descrCod.place(x=1, y=50, width=80, height=25)

        self.entradaCod = EntPlaceHold(self.janelaTec, '')
        self.entradaCod.place(x=80, y=50, width=40, height=25)

        self.descrTec = LabelGlac(self.janelaTec)
        self.descrTec.configure(text=self.m_Tecnico)
        self.descrTec.place(x=1, y=80, width=80, height=25)

        self.entradaTec = EntPlaceHold(self.janelaTec, '')
        self.entradaTec.place(x=80, y=83, width=210, height=25)

        # Widgets - Listar tecnicos
        self.listaServ = ttk.Treeview(self.janelaTec,
            height=6, column=("col1", "col2"))
        self.listaServ.heading("#0", text="")
        self.listaServ.column("#0", width=0)
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.column("#1", width=55)
        self.listaServ.heading("#2", text=self.m_Tecnico)
        self.listaServ.column("#2", width=220)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janelaTec, orient='vertical',
            command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=620, y=50, width=20, height=140)
        self.listaServ.bind("<Double-1>", self.OnDoubleClickT)

        self.conecta_Glac()

        lista = self.cursor.execute("""
                    SELECT cod, tecnico FROM tecnico  ORDER BY tecnico ASC;
                    """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.place(x=345, y=50)

        self.desconecta_Glac()

        self.janelaTec.mainloop()

