from funcs.modulos import *

class CadServ:
    def OnDoubleClickS(self, event):
        self.limpa_servicoS()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.listaServ.item(n, 'values')
            self.entradaCod.insert(END, col1)

        self.carrega_servicoS()
    def mud_servS(self):
        self.conecta_Glac()

        cod_sp = self.entradaCod.get()
        servprod = self.entradaServ.get()
        hor = self.entradaHor.get()
        custo = self.entradaCustohora.get()
        valor = self.entradaValorhora.get()
        tiposerv = self.entradaTipoServ.get()
        sistemaserv = self.entradaSistemaServ.get()
        descricao = self.entradaDescricao.get()
        veic = self.entradaVeic.get()

        self.cursor.execute("""
     		UPDATE servprod SET servprod = ? WHERE cod_sp = ?""", (servprod, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET hor = ? WHERE cod_sp = ?""", (hor, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET custo = ? WHERE cod_sp = ?""", (custo, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET valor = ? WHERE cod_sp = ?""", (valor, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET tiposerv = ? WHERE cod_sp = ?""", (tiposerv, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET sistemaserv = ? WHERE cod_sp = ?""", (sistemaserv, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET descricao = ? WHERE cod_sp = ?""", (descricao, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET id_marcaprod = ? WHERE cod_sp = ?""", (veic, cod_sp))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
         SELECT cod_sp, servprod, hor, custo , valor, descricao, id_marcaprod, tiposerv, sistemaserv FROM servprod  WHERE sp = "S" ORDER BY servprod ASC;
         """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def limpa_servicoS(self):
        self.entradaCod.delete(0, END)
        self.entradaServ.delete(0, END)
        self.entradaHor.delete(0, END)
        self.entradaCustohora.delete(0, END)
        self.entradaValorhora.delete(0, END)
        self.entradaTipoServ.delete(0, END)
        self.entradaSistemaServ.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaVeic.delete(0, END)
    def del_servS(self):
        self.conecta_Glac()

        cod_sp = self.entradaCod.get()
        self.listaServ.delete(*self.listaServ.get_children())
        self.cursor.execute("""
     	DELETE FROM servprod WHERE cod_sp=?""", (cod_sp,))
        self.conn.commit()

        lista = self.cursor.execute("""
         SELECT cod_sp, servprod, hor, custo , valor, descricao, tiposerv, sistemaserv FROM servprod  WHERE sp = "S" ORDER BY cod_sp DESC;
         """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def carrega_servicoS(self):
        cod_sp = self.entradaCod.get()
        self.conecta_Glac()

        sp = self.cursor

        self.entradaServ.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaHor.delete(0, END)
        self.entradaCustohora.delete(0, END)
        self.entradaValorhora.delete(0, END)
        self.entradaTipoServ.delete(0, END)
        self.entradaSistemaServ.delete(0, END)
        self.entradaVeic.delete(0, END)

        sp.execute("SELECT servprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaserv = self.cursor.fetchall()
        for i in consultaserv:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaServ.insert(END, i)

        hora = self.cursor
        hora.execute("SELECT hor FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultahor = self.cursor.fetchall()
        for i in consultahor:
            self.entradaHor.insert(END, i)

        custohora = self.cursor
        custohora.execute("SELECT custo FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultacustohora = self.cursor.fetchall()
        for i in consultacustohora:
            self.entradaCustohora.insert(END, i)

        valorhora = self.cursor
        valorhora.execute("SELECT valor FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultavalorhora = self.cursor.fetchall()
        for i in consultavalorhora:
            self.entradaValorhora.insert(END, i)

        tiposerv = self.cursor
        tiposerv.execute("SELECT tiposerv FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultatiposerv = self.cursor.fetchall()
        for i in consultatiposerv:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaTipoServ.insert(END, i)

        sistemaserv = self.cursor
        sistemaserv.execute("SELECT sistemaserv FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultasistemaserv = self.cursor.fetchall()
        for i in consultasistemaserv:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaSistemaServ.insert(END, i)

        descricao = self.cursor
        descricao.execute("SELECT descricao FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultadescricao = self.cursor.fetchall()
        for i in consultadescricao:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaDescricao.insert(END, i)

        self.cursor.execute("SELECT id_marcaprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultadescricao = self.cursor.fetchall()
        for i in consultadescricao:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaVeic.insert(END, i)

            self.desconecta_Glac()
    def busca_serv_veicS(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaVeic.insert(END, '%')
        veic = self.entradaVeic.get()

        self.conecta_Glac()

        servico = self.cursor

        servico.execute("""SELECT cod_sp, servprod, hor, custo, valor, descricao, id_marcaprod, tiposerv, sistemaserv
     	FROM servprod WHERE id_marcaprod LIKE '%s'  """ % veic)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaVeic.delete(0, END)

        self.desconecta_Glac()
    def busca_servicoS(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaServ.insert(END, '%')
        self.conecta_Glac()

        servprod = self.entradaServ.get()
        servico = self.cursor

        servico.execute(
            """SELECT cod_sp, servprod, hor, custo, valor, descricao, id_marcaprod, tiposerv, sistemaserv FROM servprod WHERE servprod LIKE '%s'  """ % servprod)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaServ.delete(0, END)

        self.desconecta_Glac()
    def add_servS(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        cod_sp = self.entradaCod.get()
        servprod = self.entradaServ.get()
        hor = self.entradaHor.get()
        custo = self.entradaCustohora.get()
        valor = self.entradaValorhora.get()
        tiposerv = self.entradaTipoServ.get()
        sistemaserv = self.entradaSistemaServ.get()
        descricao = self.entradaDescricao.get()
        veic = self.entradaVeic.get()
        id_marcaprod = self.entradaDescricao.get()

        self.cursor.execute("""
     		INSERT INTO servprod ( servprod, hor, custo, valor, tiposerv, sistemaserv, sp, descricao, id_marcaprod)
     		VALUES ( ?, ?, ?, ?, ?, ?, "S", ?, ?)""",
                       (servprod, hor, custo, valor, tiposerv, sistemaserv, descricao, id_marcaprod))
        self.conn.commit()
        lista = self.cursor.execute("""
         SELECT cod_sp, servprod, hor, custo , valor, descricao , id_marcaprod, tiposerv, sistemaserv FROM servprod  WHERE sp = "S" ORDER BY cod_sp DESC;
         """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()