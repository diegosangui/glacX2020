from funcs.modulos import *
from Janelas.estiloWidgets.autcomplety import *

class BuscaOrc:
    def busca_orc(self):
        ### Widgets - Listar Orçamentos ###
        self.listaOrc = Toplevel()
        self.listaOrc.title(" GLAC  ")
        self.listaOrc.configure(background= self.fg_label, bd=6)
        self.listaOrc.geometry("640x360")
        self.listaOrc.resizable(FALSE, FALSE)
        self.listaOrc.transient(self.janela)
        self.listaOrc.focus_force()
        self.listaOrc.grab_set()

        self.cliente_canvas2=Canvas(self.listaOrc,width=600,height=60,
            cursor='X_cursor',bg= self.fundo_do_frame,
            highlightbackground = self.borda_frame, highlightthickness = 3)
        self.cliente_canvas2.place(x=10, y=1)

        self.listaNomeO = Entry(self.listaOrc, width=20, justify='right', bd=2,
            fg=self.fg_entry, bg = self.bg_entry,
            font=('Verdana', '12', 'bold')); self.listaNomeO.place(x=140, y=7)

        self.botaoBuscaNome=Button(self.listaOrc,
            text=self.m_Buscar + " " + self.m_Nome, bd=1,bg=self.bg_button,
            fg = 'white', font=('verdana', '10', 'bold'),
            command=self.buscanomeorc)
        self.botaoBuscaNome.place(x=370, y=6, width=110, height = 25)

        self.listaPlaca = Entry(self.listaOrc, width=20, justify='right', bd=2,
            fg= self.fg_entry, bg= self.bg_entry,
            font=('Verdana', '12', 'bold'));self.listaPlaca.place(x=140, y=37)

        self.botaoBuscaPlaca = Button(self.listaOrc,
            text= self.m_Buscar + ' ' +self.m_Placa,bd=1,bg=self.bg_button,
            fg='white', font=('Verdana', '10', 'bold'), command=self.buscaplacaorc)
        self.botaoBuscaPlaca.place(x=370, y=36, width=110, height = 25)

        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()

        ### Widgets - Listar veiculos ###

        self.listaServ = ttk.Treeview(self.listaOrc, height=12,
            column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text= self.m_Orcamento)
        self.listaServ.heading("#2", text= self.m_Nome)
        self.listaServ.heading("#3", text= self.m_Dia)
        self.listaServ.heading("#4", text= self.m_Mes)
        self.listaServ.heading("#5", text= self.m_Ano)
        self.listaServ.heading("#6", text= self.m_Placa)
        self.listaServ.heading("#7", text= self.m_Tipo)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=40)
        self.listaServ.column("#2", width=200)
        self.listaServ.column("#3", width=35)
        self.listaServ.column("#4", width=35)
        self.listaServ.column("#5", width=55)
        self.listaServ.column("#6", width=80)
        self.listaServ.column("#7", width=137)
        # Cria barra de rolagem
        self.barra = Scrollbar(self.listaOrc, orient='vertical',
                               command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=595, y=70, width=30, height=270)

        self.listaServ.place(x=10, y=70)

        self.listaServ.bind("<Double-1>", self.carrega_orc)

        lista = cursor.execute("""
            SELECT id_orc1, clientes.nome, dia , mes , ano, placa_orc, tipoOrc 
            FROM orcamento1, clientes WHERE cod_cli = cliente_orc 
            ORDER BY id_orc1 DESC; """)
        rows = cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        conn.close()

        def busca_orc_a(event):
            busca_orc()

