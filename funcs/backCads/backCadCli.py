from Janelas.estiloWidgets.autcomplety import *
import pycep_correios

class CadCli:
    def add_autobindC(self, event):
        # codServ1.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.listatec1.selection()
        for n in self.listatec1.selection():
            col1, col2, col3 = self.listatec1.item(n, 'values')
            self.nomeEquipEntry.insert(END, col2)
            self.marcaEquipEntry.insert(END, col3)
            self.entradaVeiculo2.insert(END, col1)

        cod = self.entradaVeiculo2.get()

        self.conecta_Glac()

        self.cursor.execute(
            """SELECT montad FROM automoveis WHERE cod_aut LIKE '%s'""" % cod)
        addservico1cod = self.cursor.fetchall()
        for i in addservico1cod:
            self.marcaEquipEntry.insert(END, i)

        self.desconecta_Glac()

        self.listatec.destroy()
        ###############
    def add_clienteC(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())

        self.variaveisCliente()
        self.variaveisVeiculo()

        self.cursor.execute("""
              	INSERT INTO clientes ( nome, nascdia, nascmes, nascano, endereco, numcasa,
           	    complemento, bairro, municipio, uf, fone1ddd, fone1, fone2ddd, fone2, cep,
           	    cpf, rg, email, obs)
           	    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                            (self.cadcli_nome, self.cadcli_nascdia, self.cadcli_nascmes, self.cadcli_nascano,
                             self.cadcli_endereco, self.cadcli_numcasa, self.cadcli_complemento, self.cadcli_bairro,
                             self.cadcli_municipio, self.cadcli_uf, self.cadcli_fone1ddd, self.cadcli_fone1,
                             self.cadcli_fone2ddd, self.cadcli_fone2, self.cadcli_cep, self.cadcli_cpf,
                             self.cadcli_cnpj, self.cadcli_email, self.cadcli_obs))
        self.conn.commit()

        msg = self.m_msgClienteAdd
        msg += ""
        messagebox.showinfo("GLAC ", msg)

        lista1 = self.cursor.execute("""
        	  	SELECT  cod_cli, nome, fone1ddd, fone1 FROM clientes  ORDER BY nome ASC;
            """)
        for i in lista1:
            self.listaServ.insert("", END, values=i)
        self.conn.commit()
        self.limpa_clienteC()
        self.desconecta_Glac()
        self.janelaCli.destroy()
        self.cadcli()
    def add_veiculoC(self):
        self.variaveisCliente()
        self.variaveisVeiculo()

        cod_cli = self.codPeEntry.get()

        motor = '0'

        self.conecta_Glac()

        self.cursor.execute("""
    	    	INSERT INTO frota ( idcliente, placa, veiculo, montadora, ano, combust, cor)
    	    	VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                            (self.cadcli_cod, self.cadcli_placa, self.cadcli_montadora,
                             self.cadcli_veiculo, self.cadcli_ano, self.cadcli_combust, self.cadcli_cor))
        self.conn.commit()

        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
                    	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()

        msg = self.m_msgAutAdd
        messagebox.showinfo("GLAC ", msg)
        self.janelaCli.destroy()
        self.cadcli()
    def busca_clienteC(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())

        self.nomePeEntry.insert(END, '%')
        nome = self.nomePeEntry.get()
        self.cursor.execute(
            """SELECT cod_cli, nome, fone1ddd, fone1 FROM clientes WHERE nome LIKE '%s' ORDER BY nome ASC""" % nome)
        buscanomecli = self.cursor.fetchall()
        for i in buscanomecli:
            self.listaServ.insert("", END, values=i)

        self.limpa_clienteC()

        self.desconecta_Glac()
    def bind_autoC(self, event):
        # codServ1.delete(0, END)
        self.limpa_entryautoC()
        self.listaPlaca.selection()

        for n in self.listaPlaca.selection():
            col1, col2, col3, col4, col5, col6 = self.listaPlaca.item(n, 'values')

        self.serialEquipEntry.insert(END, col1)
        self.nomeEquipEntry.insert(END, col3)
        self.marcaEquipEntry.insert(END, col2)
        self.entradaVeiculo2.insert(END, 0)
        # self.entradaMontadora2.insert(END, col8)
        self.codEquipEntry.insert(END, 0)
        self.corvar.set(col4)
        self.combvar.set(col5)
        self.fabrAnoEquipEntry.insert(END, col6)
    def carrega_clienteC(self):
        cod_cli = self.codPeEntry.get()
        self.limpa_clienteC2()
        self.conecta_Glac()

        self.cursor.execute("SELECT UPPER(nome) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacli = self.cursor.fetchall()
        for i in consultacli:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.nomePeEntry.insert(END, i)

        self.cursor.execute("SELECT nascdia FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultadia = self.cursor.fetchall()
        for i in consultadia:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.nascDiaPeEntry.insert(END, i)

        self.cursor.execute("SELECT nascmes FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultames = self.cursor.fetchall()
        for i in consultames:
            self.nascMesPeEntry.insert(END, i)

        self.cursor.execute("SELECT nascano FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultano = self.cursor.fetchall()
        for i in consultano:
            self.nascAnoPeEntry.insert(END, i)

        self.cursor.execute("SELECT numcasa FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultanum = self.cursor.fetchall()
        for i in consultanum:
            self.numPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(complemento) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacompl = self.cursor.fetchall()
        for i in consultacompl:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.complemPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(email) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultaemail = self.cursor.fetchall()
        for i in consultaemail:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.emailPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(endereco) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultaend = self.cursor.fetchall()
        for i in consultaend:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.logradPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(bairro) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultabairro = self.cursor.fetchall()
        for i in consultabairro:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.bairroPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(municipio) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultamunicipio = self.cursor.fetchall()
        for i in consultamunicipio:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.cidadePeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(uf) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultauf = self.cursor.fetchall()
        for i in consultauf:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.ufPeEntry.insert(END, i)

        self.cursor.execute("SELECT fone1ddd FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone1ddd = self.cursor.fetchall()
        for i in consultafone1ddd:
            self.fone1PeEntry.insert(END, i)

        self.cursor.execute("SELECT fone1 FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone1 = self.cursor.fetchall()
        for i in consultafone1:
            self.fone1PeEntry2.insert(END, i)

        self.cursor.execute("SELECT fone2ddd FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone2ddd = self.cursor.fetchall()
        for i in consultafone2ddd:
            self.fone2PeEntry.insert(END, i)

        self.cursor.execute("SELECT fone2 FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone2 = self.cursor.fetchall()
        for i in consultafone2:
            self.fone2PeEntry2.insert(END, i)

        self.cursor.execute("SELECT cep FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacep = self.cursor.fetchall()
        for i in consultacep:
            self.cepPeEntry.insert(END, i)

        self.cursor.execute("SELECT cpf FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacpf = self.cursor.fetchall()
        for i in consultacpf:
            self.cpfPeEntry.insert(END, i)

        self.cursor.execute("SELECT rg FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultarg = self.cursor.fetchall()
        for i in consultarg:
            self.cnpjPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(obs) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultaobs = self.cursor.fetchall()
        for i in consultaobs:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.obsPeEntry.insert(END, i)

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
    	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()
    def OnVsbC(self, *args):
        self.listaServ.yview(*args)
    def OnMouseWheelC(self, event):
        self.listaServ.yview("scroll", event.delta, "units")

        return "break"
    def OnDoubleClickC(self, *args):
        self.limpa_clienteC()

        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4 = self.listaServ.item(n, 'values')
            self.codPeEntry.insert(END, col1)

        self.carrega_clienteC()
    def mud_autoC(self):
        self.variaveisCliente()
        self.variaveisVeiculo()

        cod_cli = self.codPeEntry.get()
        self.conecta_Glac()

        self.cursor.execute(""" UPDATE frota SET veiculo = ?, ano = ?, placa = ?,
            idcliente = ?, combust = ?, montadora = ?, cor = ? WHERE placa = ? AND idcliente = ?""",
                            (self.cadcli_veiculo, self.cadcli_ano, self.cadcli_placa, cod_cli,
                             self.cadcli_combust, self.cadcli_montadora,
                             self.cadcli_cor, self.cadcli_placa, cod_cli))
        self.conn.commit()

        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
            	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()
        msg = self.m_msgVeiculoAlt
        msg += ""
        messagebox.showinfo("GLAC ", msg)
        self.carrega_clienteC()
        self.janelaCli.destroy()
        self.cadcli()
    def mud_clienteC(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.conecta_Glac()

        self.variaveisCliente()
        self.variaveisVeiculo()

        self.cursor.execute("""
    	    UPDATE clientes SET nome = ?, endereco = ?, bairro = ?, municipio = ?,
    	    uf = ?, cep = ?, cpf = ?, rg = ?, obs = ?, email = ?, fone1ddd = ?, fone1 = ?,
    	    fone2ddd = ?, fone2 = ?, complemento = ?, numcasa = ?, nascdia = ?, nascmes = ?, nascano = ?
    	    WHERE cod_cli = ?""",
                            (self.cadcli_nome, self.cadcli_endereco, self.cadcli_bairro, self.cadcli_municipio,
                             self.cadcli_uf, self.cadcli_cep, self.cadcli_cpf, self.cadcli_cnpj, self.cadcli_obs,
                             self.cadcli_email, self.cadcli_fone1ddd, self.cadcli_fone1, self.cadcli_fone2ddd,
                             self.cadcli_fone2, self.cadcli_complemento, self.cadcli_numcasa, self.cadcli_nascdia,
                             self.cadcli_nascmes, self.cadcli_nascano, self.cadcli_cod))
        self.conn.commit()

        lista = self.cursor.execute("""SELECT cod_cli, nome, fone1ddd, fone1 FROM clientes ORDER BY nome ASC;
    	    	""")

        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()

        msg = self.m_msgClienteAlt
        msg += ""
        messagebox.showinfo("GLAC - Clientes", msg)
        self.janelaCli.destroy()
        self.cadcli()
    def limpa_entryautoC(self):
        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        # self.corEquipEntry.delete(0, END)
        # self.combEquipEntry.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
    def limpa_clienteC(self):
        self.codPeEntry.delete(0, END)
        self.limpa_clienteC2()
    def limpa_clienteC2(self):
        # self.codPeEntry.delete(0, END)
        self.nomePeEntry.delete(0, END)
        self.nascDiaPeEntry.delete(0, END)
        self.nascMesPeEntry.delete(0, END)
        self.nascAnoPeEntry.delete(0, END)
        self.logradPeEntry.delete(0, END)
        self.numPeEntry.delete(0, END)
        self.complemPeEntry.delete(0, END)
        self.bairroPeEntry.delete(0, END)
        self.cidadePeEntry.delete(0, END)
        self.ufPeEntry.delete(0, END)
        self.fone1PeEntry.delete(0, END)
        self.fone1PeEntry2.delete(0, END)
        self.fone2PeEntry.delete(0, END)
        self.fone2PeEntry2.delete(0, END)
        self.cepPeEntry.delete(0, END)
        self.cnpjPeEntry.delete(0, END)
        self.cpfPeEntry.delete(0, END)
        self.obsPeEntry.delete(0, END)
        self.emailPeEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.limpa_entryautoC()
    def del_clienteC(self):
        self.conecta_Glac()
        self.listaServ.delete(*self.listaServ.get_children())
        self.listaPlaca.delete(*self.listaPlaca.get_children())
        cod_cli = self.codPeEntry.get()
        self.cursor.execute("""
            	DELETE FROM frota WHERE idcliente=?""", (cod_cli,))
        self.conn.commit()
        self.cursor.execute("""
    	        DELETE FROM clientes WHERE cod_cli=?""", (cod_cli,))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        self.listaPlaca.delete(*self.listaPlaca.get_children())
        lista = self.cursor.execute("""
    		SELECT cod_cli, nome, fone1ddd, fone1 FROM clientes  ORDER BY nome ASC
    	""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.limpa_clienteC()

        self.desconecta_Glac()
        self.listatec.destroy()
    def del_placaC(self):
        self.listaPlaca.delete(*self.listaPlaca.get_children())
        cod_cli = self.codPeEntry.get()
        placa = self.serialEquipEntry.get()
        self.conecta_Glac()

        self.cursor.execute("""
            	DELETE FROM frota 
            	WHERE placa =? AND idcliente = ?""", (placa, cod_cli))
        self.conn.commit()

        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
            	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()
        self.limpa_entryautoC()
        self.listatec.destroy()
    def variaveisCliente(self):
        self.cadcli_cod = self.codPeEntry.get()
        self.cadcli_nome = self.nomePeEntry.get()
        self.cadcli_nascdia = self.nascDiaPeEntry.get()
        self.cadcli_nascmes = self.nascMesPeEntry.get()
        self.cadcli_nascano = self.nascAnoPeEntry.get()
        self.cadcli_endereco = self.logradPeEntry.get()
        self.cadcli_numcasa = self.numPeEntry.get()
        self.cadcli_complemento = self.complemPeEntry.get()
        self.cadcli_bairro = self.bairroPeEntry.get()
        self.cadcli_municipio = self.cidadePeEntry.get()
        self.cadcli_uf = self.ufPeEntry.get()
        self.cadcli_fone1ddd = self.fone1PeEntry.get()
        self.cadcli_fone1 = self.fone1PeEntry2.get()
        self.cadcli_fone2ddd = self.fone2PeEntry.get()
        self.cadcli_fone2 = self.fone2PeEntry2.get()
        self.cadcli_cep = self.cepPeEntry.get()
        self.cadcli_cpf = self.cpfPeEntry.get()
        self.cadcli_cnpj = self.cnpjPeEntry.get()
        self.cadcli_email = self.emailPeEntry.get()
        self.cadcli_obs = self.obsPeEntry.get()
    def variaveisVeiculo(self):
        self.cadcli_veiculoId = self.codEquipEntry.get()
        self.cadcli_MontadoraId = self.entradaMontadora2.get()
        self.cadcli_veiculo = self.nomeEquipEntry.get()
        self.cadcli_ano = self.fabrAnoEquipEntry.get()
        self.cadcli_placa = self.serialEquipEntry.get()
        self.cadcli_montadora = self.marcaEquipEntry.get()
        self.cadcli_combust = self.combvar.get()
        self.cadcli_cor = self.corvar.get()
    def cep(self):
        self.logradPeEntry.delete(0, END)
        self.bairroPeEntry.delete(0, END)
        self.cidadePeEntry.delete(0, END)
        self.ufPeEntry.delete(0, END)
        try:
            self.cep = self.cepPeEntry.get()
            endcep = pycep_correios.get_address_from_cep(self.cep)
            self.logradPeEntry.insert(END, endcep['logradouro'])
            self.bairroPeEntry.insert(END, endcep['bairro'])
            self.cidadePeEntry.insert(END, endcep['cidade'])
            self.ufPeEntry.insert(END, endcep['uf'])
        except:
            messagebox.showinfo("GLAC", 'Cep não encontrado')
