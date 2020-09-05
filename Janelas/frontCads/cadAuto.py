from funcs.backCads.backCadAuto import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.labelStyle import LabelGlac
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *

class Automoveis(cadAuto):
    def cadaut(self):
        self.telaAut()
        self.canvasAut()
    def telaAut(self):
        self.janelaAut = Toplevel()
        self.janelaAut.title('Glac')
        self.janelaAut.configure(background=self.fundo_da_tela)
        self.janelaAut.geometry("800x235")
        self.janelaAut.resizable(FALSE, FALSE)
        self.janelaAut.transient(self.janela)
        self.janelaAut.focus_force()
        self.janelaAut.grab_set()

        self.background_label = Label(self.janelaAut,
            image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)
    def canvasAut(self):
        self.autoGrad = GradientFrame(self.janelaAut)
        self.autoGrad.place(relx=0.01, rely=0.12,
            relwidth=0.98, relheight=0.85)

        # Label do codigo
        self.descrCod_aut = LabelGlac(self.janelaAut)
        self.descrCod_aut.configure(text=self.m_Codigo)
        self.descrCod_aut.place(x=10, y=52, width=90)

        #### entrada do codigo
        self.entradaCod_autA = EntPlaceHold(self.janelaAut, '')
        self.entradaCod_autA.configure(validate="key",
            validatecommand=self.vcmd4)
        self.entradaCod_autA.place(x=85, y=52, width=40)

        # descrição do veiculo
        self.descrAut = LabelGlac(self.janelaAut)
        self.descrAut.configure(text=self.m_Automovel)
        self.descrAut.place(x=10, y=90)

        self.entradaAutA = EntPlaceHold(self.janelaAut, '')
        self.entradaAutA.configure(width=22)
        self.entradaAutA.place(x=95, y=90)

        #### entry da marca
        self.entradaMarcaA = EntPlaceHold(self.janelaAut, '')
        self.entradaMarcaA.configure(width=28)
        self.entradaMarcaA.place(x=85, y=130)

        self.entradaMarca2A = Entry(width=20)

        ##### label do titulo da janela
        self.descrNomeServ = LabelGlac(self.janelaAut)
        self.descrNomeServ.configure(text=self.m_Automoveis)
        self.descrNomeServ.place(relx=0.4, rely=0,
                                 relwidth= 0.2,relheight=0.1)

        ###### botão busca
        self.botaoBuscaAut = ButtonGlac(self.janelaAut)
        self.botaoBuscaAut.configure(text=self.m_Buscar,
                                     command=self.busca_automovelA)
        self.botaoBuscaAut.place(x=290, y=89, width=65, height=23)

        ##### botao Carregar
        self.botaoCarregaAut = ButtonGlac(self.janelaAut)
        self.botaoCarregaAut.configure(text=self.m_Carregar,
                            command=self.carrega_automovelA)
        self.botaoCarregaAut.place(x=150, y=50, width=90)

        ##### botao limpa
        self.botaoLimpaAut = ButtonGlac(self.janelaAut)
        self.botaoLimpaAut.configure(text=self.m_Limpar,
                            command=self.limpa_automovelA)
        self.botaoLimpaAut.place(x=250, y=50, width=90)

        #### botao marca
        self.botaoMarcaAut = ButtonGlac(self.janelaAut)
        self.botaoMarcaAut.configure(text=self.m_Marca,
                            command=self.busca_autoA)
        self.botaoMarcaAut.place(x=10, y=128,
            width=72, height=23)

        #####
        self.botaoNovoAut = ButtonGlac(self.janelaAut)
        self.botaoNovoAut.configure(text=self.m_Novo,
                            command=self.add_automovelA)
        self.botaoNovoAut.place(x=30, y=180, width=80)

        #####
        self.botaoAlterarAut = ButtonGlac(self.janelaAut)
        self.botaoAlterarAut.configure(text=self.m_Alterar,
                                command=self.mud_automovelA)
        self.botaoAlterarAut.place(x=130, y=180, width=80)

        #####
        self.botaoApagarAut = ButtonGlac(self.janelaAut)
        self.botaoApagarAut.configure(text=self.m_Apagar,
                                command=self.del_automovelA)
        self.botaoApagarAut.place(x=230, y=180, width=80)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janelaAut,
            orient='vertical', command=self.OnVsbA)

        # Widgets - Listar veiculos
        self.listaServ = ttk.Treeview(self.janelaAut, height=8,
                                column=("col1", "col2", "col3"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Automovel)
        self.listaServ.heading("#3", text=self.m_Marca)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=45)
        self.listaServ.column("#2", width=180)
        self.listaServ.column("#3", width=170)
        self.listaServ.configure(yscroll=self.barra.set)
        self.listaServ.place(x=365, y=40)

        # Adiciona barra de rolagem
        self.barra.place(x=765, y=40, width=20, height=185)

        self.busca_automovelA()
        ###
        ''' Função de duplo clique na lista para carregar os dados da seleção
        na tela de cadastro'''
        self.listaServ.bind("<Double-1>", self.OnDoubleClickA)
        ###

        self.janelaAut.mainloop()
    def busca_autoA(self):
        # Widgets -
        self.entradaMarcaA.insert(0, '%')
        veicAuto = self.entradaMarcaA.get()

        self.listatec = Toplevel()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("320x220")
        self.listatec.resizable(FALSE, FALSE)
        self.listatec.transient(self.janelaAut)
        self.listatec.focus_force()
        self.listatec.grab_set()

        ### Widgets -
        self.listaTec1 = ttk.Treeview(self.listatec, height=5,
                                      column=("col1", "col2"))
        self.listaTec1.heading("#0", text="")
        self.listaTec1.heading("#1", text=self.m_Codigo)
        self.listaTec1.heading("#2", text='Marca')

        self.listaTec1.column("#0", width=0)
        self.listaTec1.column("#1", width=60)
        self.listaTec1.column("#2", width=200)

        self.barra.place(relx=0.9, rely=0.1,
                         relwidth=0.1, relheight=0.8)
        # Adiciona barra de rolagem
        self.listaTec1.configure(yscroll=self.barra.set)
        self.listaTec1.place(relx=0.1, rely=0.1,
                             relwidth= 0.8, relheight=0.8)
        # Binding da listbox
        self.listaTec1.bind('<Double-1>', self.add_autobindA)

        self.conecta_Glac()

        buscaservico = self.cursor.execute("""SELECT cod, marca 
            FROM montadora 
            WHERE marca LIKE '%s' ORDER BY marca ASC""" % veicAuto)

        for i in buscaservico:
            self.listaTec1.insert("", END, values=i)

        self.entradaMarcaA.delete('0', 'end')
        self.entradaMarca2A.delete('0', 'end')

        self.desconecta_Glac()
