from funcs.modulos import *
from Janelas.estiloWidgets.autcomplety import *

class Busca_Serv:
    def busca_servico(self):
        ### Widgets - Listar Produtos e Serviços ###
        self.listaServP1 = Toplevel()
        self.listaServP1.title(self.m_PesquisaServProd)
        self.listaServP1.geometry("950x280")
        self.listaServP1.configure(background= self.fg_label)
        self.listaServP1.resizable(FALSE, FALSE)
        self.listaServP1.transient(self.janela)
        self.listaServP1.focus_force()
        self.listaServP1.grab_set()

        self.barra12 = Scrollbar(self.listaServP1, orient='vertical',
                                 command=self.OnVsb_S1)
        self.barra12.place(x=920, y=41, width=25, height=226)

        self.listaServ1 = ttk.Treeview(self.listaServP1, height=10,
            yscrollcommand=self.barra12.set,
            column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))

        self.listaServ1.heading("#0", text="")
        self.listaServ1.column("#0", width=0)
        self.listaServ1.heading("#1", text= self.m_Codigo);
        self.listaServ1.column("#1", width=45)
        self.listaServ1.heading("#2", text= self.m_Serviços +
                                            self.m_barra + self.m_Produtos);
        self.listaServ1.column("#2", width=250)
        self.listaServ1.heading("#3", text= self.m_Tipo);
        self.listaServ1.column("#3", width=120)
        self.listaServ1.heading("#4", text= self.m_Quant);
        self.listaServ1.column("#4", width=50)
        self.listaServ1.heading("#5", text= self.m_Marca);
        self.listaServ1.column("#5", width=90)
        self.listaServ1.heading("#6", text= self.m_Automovel);
        self.listaServ1.column("#6", width=140)
        self.listaServ1.heading("#7", text= self.m_Sistema);
        self.listaServ1.column("#7", width=140)
        self.listaServ1.heading("#8", text= self.m_Valor);
        self.listaServ1.column("#8", width=70)

        self.listaServ1.place(x=15, y=40)
        self.listaServ1.configure(yscroll=self.barra12.set)
        self.listaServ1.delete(*self.listaServ1.get_children())

        self.descrCod_cli=Label(self.listaServP1,text=self.m_Pesquisa +
            self.m_Pontinhos, fg= self.fg_label, bg= self.bg_label,
            font=('Verdana', '8', 'bold')).place(x=20, y=7, height = 30)
        self.listaServicos1 = Entry(self.listaServP1, width=20, justify='right',
            bd=3, fg='brown', font=('Verdana', '12', 'bold'))
        self.listaServicos1.place(x=120, y=7, height = 30)

        self.botaoBuscaServicos1 = Button(self.listaServP1,
            text= self.m_BuscaServProd, bd=2, bg ='#178bca', fg ='white',
            font=('Verdana', '9', 'bold'), command=self.busca_serv)
        self.botaoBuscaServicos1.place(x=350, y=7, width=200, height = 30)

        self.botaoBuscaServicos2 = Button(self.listaServP1,
            text= self.m_BuscaVeiculos, bd=2, bg ='#178bca', fg ='white',
            font=('Verdana', '9', 'bold'), command=self.busca_serv_veic)
        self.botaoBuscaServicos2.place(x=570, y=7, width=120, height = 30)
        servprod = self.listaServicos1.get()

        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()

        cursor.execute(
            """SELECT cod_sp, servprod, tiposerv, hor, descricao, id_marcaprod, 
            sistemaserv, valor * hor
            FROM servprod ORDER BY cod_sp ASC""")
        buscaservico12 = cursor.fetchall()
        for i in buscaservico12:
            self.listaServ1.insert("", END, values=i)
        conn.close()
