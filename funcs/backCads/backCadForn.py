from Janelas.estiloWidgets.autcomplety import *

class CadForn():
    def OnDoubleClickForn(self, event):
        self.limpa_fornecedor()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServ.item(n, 'values')
            self.entradaCod_forn.insert(END, col1)
        self.carrega_fornecedor()
    def mud_fornec(self):
        self.conecta_Glac()

        cod_forn = self.entradaCod_forn.get()
        fornecedor = self.entradaFornecedor.get()
        fone = self.entradaFone.get()
        cnpj = self.entradaCnpj.get()
        cep = self.entradaCep.get()
        endereco = self.entradaEndereco.get()
        municipio = self.entradaMunicipio.get()
        descricao = self.entradaDescricao.get()

        self.cursor.execute("""
    		UPDATE fornecedores SET fornecedor = ? WHERE cod_forn = ?""",
                            (fornecedor, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET fone = ? WHERE cod_forn = ?""",
                            (fone, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET cnpj = ? WHERE cod_forn = ?""",
                            (cnpj, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET cep = ? WHERE cod_forn = ?""",
                            (cep, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET endereco = ? WHERE cod_forn = ?""",
                            (endereco, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET municipio = ? WHERE cod_forn = ?""",
                            (municipio, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET descricao = ? WHERE cod_forn = ?""",
                            (descricao, cod_forn))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao 
        FROM fornecedores ORDER BY fornecedor ASC;
        """)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
            self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
    		SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao 
    		FROM fornecedores ORDER BY fornecedor ASC;
    		""")
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        self.desconecta_Glac()
        msg = "Dados do fornecedor alterados com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def limpa_fornecedor(self):
        self.conecta_Glac()
        self.entradaCod_forn.delete(0, END)
        self.entradaFornecedor.delete(0, END)
        self.entradaFone.delete(0, END)
        self.entradaCnpj.delete(0, END)
        self.entradaCep.delete(0, END)
        self.entradaEndereco.delete(0, END)
        self.entradaMunicipio.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.desconecta_Glac()
    def del_fornec(self):
        self.conecta_Glac()

        cod_forn = self.entradaCod_forn.get()
        self.cursor.execute(
            """DELETE FROM fornecedores WHERE cod_forn=?""", (cod_forn,))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute(
            """SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao 
            FROM fornecedores ORDER BY fornecedor ASC;""")

        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        self.desconecta_Glac()
        msg = "Fornecedor excluido com sucesso.  :("
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def carrega_fornecedor(self):
        self.conecta_Glac()

        cursor = self.cursor

        cod_forn = self.entradaCod_forn.get()
        fornec = cursor

        self.entradaFornecedor.delete(0, END)
        self.entradaFone.delete(0, END)
        self.entradaCnpj.delete(0, END)
        self.entradaCep.delete(0, END)
        self.entradaEndereco.delete(0, END)
        self.entradaMunicipio.delete(0, END)
        self.entradaDescricao.delete(0, END)

        fornec.execute("SELECT fornecedor FROM fornecedores "
                       "WHERE cod_forn = '%s'" % cod_forn)
        consultafornec = self.cursor.fetchall()
        for i in consultafornec:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaFornecedor.insert(END, i)

        fone = self.cursor
        fone.execute("SELECT fone FROM fornecedores "
                     "WHERE cod_forn = '%s'" % cod_forn)
        consultafone = self.cursor.fetchall()
        for i in consultafone:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaFone.insert(END, i)

        cnpj = self.cursor
        cnpj.execute("SELECT cnpj FROM fornecedores "
                     "WHERE cod_forn = '%s'" % cod_forn)
        consultacnpj = self.cursor.fetchall()
        for i in consultacnpj:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaCnpj.insert(END, i)

        cep = cursor
        cep.execute("SELECT cep FROM fornecedores "
                    "WHERE cod_forn = '%s'" % cod_forn)
        consultacep = cursor.fetchall()
        for i in consultacep:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaCep.insert(END, i)

        endereco = cursor
        endereco.execute("SELECT endereco FROM fornecedores "
                         "WHERE cod_forn = '%s'" % cod_forn)
        consultaendereco = cursor.fetchall()
        for i in consultaendereco:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaEndereco.insert(END, i)

        municipio = cursor
        municipio.execute("SELECT municipio FROM fornecedores "
                          "WHERE cod_forn = '%s'" % cod_forn)
        consultamunicipio = cursor.fetchall()
        for i in consultamunicipio:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMunicipio.insert(END, i)

        descricao = cursor
        descricao.execute(
            "SELECT descricao FROM fornecedores "
            "WHERE cod_forn = '%s'" % cod_forn)
        consultadescricao = cursor.fetchall()
        for i in consultadescricao:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaDescricao.insert(END, i)

        self.desconecta_Glac()
    def cepForn(self):
        self.entradaEndereco.delete(0, END)
        self.entradaMunicipio.delete(0, END)

        try:
            self.cep = self.entradaCep.get()
            self.endereco = pycep_correios.consultar_cep(self.cep)

            self.entradaEndereco.insert(END, self.endereco['end'])
            self.entradaEndereco.insert(END, ' - ')
            self.entradaEndereco.insert(END, self.endereco ['bairro'])

            self.entradaMunicipio.insert(END, self.endereco['cidade'])
            self.entradaMunicipio.insert(END, ' - ')
            self.entradaMunicipio.insert(END, self.endereco['uf'])


        except ExcecaoPyCEPCorreios as exc:
            msg = multi.CepNotFind
            msg += ""
            messagebox.showinfo("GLAC ", msg)
    def busca_fornecedor(self):
        self.conecta_Glac()

        self.entradaFornecedor.insert(END, '%')
        self.listaServ.delete(*self.listaServ.get_children())
        fornecedor = self.entradaFornecedor.get()

        lista = self.cursor.execute(
            """SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao 
            FROM fornecedores WHERE fornecedor LIKE '%s' 
            ORDER BY fornecedor ASC;""" % fornecedor)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
            self.entradaFornecedor.delete(0, END)
        self.desconecta_Glac()
    def add_fornec(self):
        self.conecta_Glac()
        self.listaServ.delete(*self.listaServ.get_children())
        cod_forn = self.entradaCod_forn.get()
        fornecedor = self.entradaFornecedor.get()
        fone = self.entradaFone.get()
        cnpj = self.entradaCnpj.get()
        cep = self.entradaCep.get()
        endereco = self.entradaEndereco.get()
        municipio = self.entradaMunicipio.get()
        descricao = self.entradaDescricao.get()

        self.cursor.execute(
            """INSERT INTO fornecedores 
            (fornecedor, fone, cnpj, cep, endereco, municipio, descricao)
            VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
            (fornecedor, fone, cnpj, cep, endereco, municipio, descricao))
        self.conn.commit()
        lista=self.cursor.execute(
            """SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao 
            FROM fornecedores ORDER BY fornecedor ASC;""")
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        msg = "Novo fornecedor incluido com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
        self.desconecta_Glac()
