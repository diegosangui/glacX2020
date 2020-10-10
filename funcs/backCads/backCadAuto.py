from Janelas.estiloWidgets.autcomplety import *

del1 = "0"
del2 = "end"

class cadAuto:

    def formatastring(self, i):
        self.i = self.i.replace('(', '')
        self.i = self.i.replace(')', '')
        self.i = self.i.replace("'", "")
        self.i = self.i.replace(',', '')
        self.i = self.i.replace('{', '')
        self.i = self.i.replace('}', '')

    def variaveisa(self):
        self.cod_aut = self.entradaCod_autA.get()
        self.automovel = self.entradaAutA.get()
        self.montad = self.entradaMarca2A.get()

    def addautomovela(self):
        self.variaveisA()
        self.conecta_Glac()
        if self.montad == '':
            msg = "É necessário escolher a marca do \n " \
                  "automovel a ser cadastrado."
            messagebox.showinfo("GLAC - Automovel", msg)
            self.desconecta_Glac()
        else:
            self.cursor.execute("""
                INSERT INTO automoveis ( automovel, montad)
                VALUES ( ?, ?)""", (self.automovel, self.montad))
            self.conn.commit()
            self.desconecta_Glac()
            self.limpa_automovelA()
            self.busca_automovelA()
            msg = self.m_msgAutAdd
            msg += ""
            messagebox.showinfo("GLAC - Automovel", msg)

    def mudautomovela(self):
        self.variaveisA()
        self.conecta_Glac()

        self.cursor.execute("""
       		UPDATE automoveis SET automovel = ? WHERE cod_aut = ?""",
            (self.automovel, self.cod_aut))
        self.conn.commit()

        self.cursor.execute("""
       		UPDATE automoveis SET montad = ? WHERE cod_aut = ?""",
            (self.montad, self.cod_aut))
        self.conn.commit()
        self.desconecta_Glac()

        self.busca_automovelA()

        msg = self.m_msgAutAlt
        msg += ""
        messagebox.showinfo("GLAC - Altera Automovel", msg)

    def delautomovela(self):
        self.variaveisA()
        self.conecta_Glac()

        self.cursor.execute(""" DELETE FROM automoveis 
            WHERE cod_aut=?;""", (self.cod_aut,))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor
        self.cursor.execute("""
            SELECT automoveis.cod_aut, automoveis.automovel, montadora.marca 
            FROM automoveis, montadora
       		WHERE montadora.cod = automoveis.montad  
       		ORDER BY automovel ASC;
       		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        self.limpa_automovelA()
        msg = self.m_msgAutDel
        msg += ""
        messagebox.showinfo("GLAC - Altera Automovel", msg)

    def carregaautomovela(self):
        cod_aut = self.entradaCod_autA.get()
        self.conecta_Glac()

        nomeaut = self.cursor

        self.entradaAutA.delete('0', 'end')
        self.entradaMarcaA.delete('0', 'end')
        self.entradaMarca2A.delete('0', 'end')

        nomeaut.execute(
            "SELECT automovel FROM automoveis, montadora "
            "WHERE montadora.cod = automoveis.montad "
            "AND cod_aut = '%s'" % cod_aut)
        consultaautomovel = self.cursor.fetchall()
        for self.i in consultaautomovel:
            self.i = str(self.i)
            self.formataString(self.i)
            self.entradaAutA.insert(0, self.i)
            print(self.i)

        nomemarca = self.cursor
        nomemarca.execute(
            "SELECT marca FROM automoveis, montadora "
            "WHERE montadora.cod = automoveis.montad "
            "AND cod_aut = '%s'" % cod_aut)
        consultamarca = self.cursor.fetchall()
        for self.i in consultamarca:
            self.i = str(self.i)
            self.formataString(self.i)
            self.entradaMarcaA.insert(0, self.i)
            print(self.i)

        nomemarca2 = self.cursor
        nomemarca2.execute(
            "SELECT montad FROM automoveis, montadora "
            "WHERE montadora.cod = automoveis.montad "
            "AND cod_aut = '%s'" % cod_aut)
        consultamarca2 = self.cursor.fetchall()
        for self.i in consultamarca2:
            self.i = str(self.i)
            self.formataString(self.i)
            self.entradaMarca2A.insert(0, self.i)
            print(self.i)

        self.desconecta_Glac()

    def buscaautomovela(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.conecta_Glac()

        self.entradaAutA.insert(0, '%')
        autom = self.entradaAutA.get()

        lista = self.cursor.execute("""
            SELECT automoveis.cod_aut, automoveis.automovel, montadora.marca 
            FROM automoveis, montadora
       		WHERE montadora.cod = automoveis.montad  
       		ORDER BY automovel ASC; """ )
        for i in lista:
            self.listaServ.insert("", 0, values=i)
        self.limpa_automovelA()
        self.desconecta_Glac()

    def ondoubleclicka(self, event):
        self.limpa_automovelA()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3 = self.listaServ.item(n, 'values')
            self.entradaCod_autA.insert(0, col1)

        self.carrega_automovelA()

    def OnVsbA(self, *args):
        self.listaServ.yview(*args)

    def addautobinda(self, event):
        for n in self.listaTec1.selection():
            col1, col2 = self.listaTec1.item(n, 'values')
            self.entradaMarca2A.insert(0, col1)
            self.entradaMarcaA.insert(0, col2)
        self.listatec.destroy()

    def limpaautomovela(self):
        self.entradaCod_autA.delete(del1, del2)
        self.entradaAutA.delete(del1, del2)
        self.entradaMarcaA.delete(del1, del2)
        self.entradaMarca2A.delete(del1, del2)