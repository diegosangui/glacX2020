from funcs.modulos import *
from Janelas.estiloWidgets.autcomplety import *

class BuscaTecnico:
    def busca_tecnico(self):
        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()
        ### Widgets - Listar tecnicos ###
        self.entradaTecnico.delete(0, END)
        self.listatec = Toplevel()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("360x160")
        self.listatec.resizable(TRUE, TRUE)
        self.listatec.transient(self.janela)
        self.listatec.focus_force()
        self.listatec.grab_set()

        self.listaServ = ttk.Treeview(self.listatec, height=6,
                                      column=("col1", "col2"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text= self.m_Codigo)
        self.listaServ.heading("#2", text= self.m_Tecnico)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=40)
        self.listaServ.column("#2", width=280)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.listatec, orient='vertical',
                               command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=325, y=5, width=30, height=145)

        self.listaServ.place(x=5, y=5)

        lista = cursor.execute("""
                SELECT cod, tecnico FROM tecnico ORDER BY cod ASC;
                """)
        rows = cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        # Binding da listbox
        self.listaServ.bind('<Double-1>', self.add_tecnicobind)
        conn.close()
