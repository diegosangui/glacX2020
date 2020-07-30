from funcs.modulos import *
from Janelas.estiloWidgets.autcomplety import *
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.labelStyle import *
from Janelas.estiloWidgets.buttonStyle import *

class BuscaCliente:
    def busca_cliente(self):
        self.listacliente = Toplevel()
        self.listacliente.title("  GLAC  ")
        self.listacliente.configure(background=self.fundo_da_tela)
        self.listacliente.geometry("342x390")
        self.listacliente.resizable(FALSE, FALSE)
        self.listacliente.transient(self.janela)
        self.listacliente.focus_force()
        self.listacliente.grab_set()

        frame1 = GradientFrame(self.listacliente)
        frame1.place(relx=0, rely=0,
                     relwidth=1, relheight=1)

        self.LabelCliente = LabelGlac(self.listacliente)
        self.LabelCliente.configure(text=self.m_BuscaCliMsg1,
                                  font=('Verdana', '8', 'bold'))
        self.LabelCliente.place(relx=0.04, rely=0.01,
                                relwidth=0.9, relheight=0.06)

        self.LabelCliente2 = LabelGlac(self.listacliente)
        self.LabelCliente2.configure(text=self.m_BuscaCliMsg2,
                                  font=('Verdana', '8', 'bold'))
        self.LabelCliente2.place(relx=0.04, rely=0.05,
                                 relwidth=0.9, relheight=0.05)

        self.LabelCliente2 = LabelGlac(self.listacliente)
        self.LabelCliente2.configure(text=self.m_Pesquisa
            + self.m_Pontinhos, font=('Verdana', '8', 'bold'))
        self.LabelCliente2.place(x=10, y=46)

        self.EntryCliente2 = Entry(self.listacliente, font=('Verdana', '8'))
        self.EntryCliente2.place(x=80, y=45)

        self.ButtonCliente2 = ButtonGlac(self.listacliente)
        self.ButtonCliente2.configure(text= self.m_Buscar,
                                    font=('Verdana', '8', 'bold'),
                                    command = self.buscaCli)
        self.ButtonCliente2.place(x=240, y=43)


        self.listaServ = ttk.Treeview(self.listacliente, height=12,
                                      column=("col1", "col2"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text= self.m_Codigo)
        self.listaServ.heading("#2", text= self.m_Nome)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=60)
        self.listaServ.column("#2", width=245)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.listacliente, orient='vertical',
                               command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=310, y=70,
                         width=20, height=262)

        self.listaServ.place(x=7, y=70)
        self.listaServ.bind("<Double-1>", self.carrega_cliente2)

        self.ButtonClienteNovo = ButtonGlac(self.listacliente)
        self.ButtonClienteNovo.configure(text="Novo",
                                font=('Verdana', '8', 'bold'),
                                command=self.cadcli)
        self.ButtonClienteNovo.place(x=10, y=350)

        self.LabelCliente2 = LabelGlac(self.listacliente)
        self.LabelCliente2.configure(text=self.m_BuscaCliMsg3,
                                   font=('Verdana', '8', 'bold'))
        self.LabelCliente2.place(relx=0.2, rely=0.88,
                                 relwidth=0.75, relheight=0.05)
        self.LabelCliente2 = LabelGlac(self.listacliente)
        self.LabelCliente2.configure(text=self.m_BuscaCliMsg4,
                                   font=('Verdana', '8', 'bold'))
        self.LabelCliente2.place(relx=0.2, rely=0.93,
                                 relwidth=0.75, relheight=0.05)

        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()

        nome = self.listNome.get()
        nomecod = cursor

        lista = cursor.execute("""SELECT cod_cli, nome FROM clientes """ )
        rows = cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
        conn.close()

        def busca_cliente_a(event):
            busca_cliente()
