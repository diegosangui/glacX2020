from tkinter import *
from tkinter import messagebox
import webbrowser

class Functions:
    def moedaTotaliza(self, totalizador=0, moeda='R$'):
        return f'{moeda}{totalizador:>8.2f}'.replace('.',',')
    def moedaTotalizador(self, totalizador=0, moeda='R$'):
        return f'{moeda}{totalizador:>8.2f}'.replace('.',',')
    def moedaTotal1(self, total1=0, moeda='R$'):
        return f'{moeda}{self.total1:>8.2f}'.replace('.',',')
    def moedaTotal2(self, total1=0):
        return f'{self.total1:>8.2f}'.replace('.', ',')
    def atualiza_listaServProd(self):
        id_orc = self.listaNumOrc.get()
        cod_item1 = self.codServ1.get()
        desc_item1 = self.listaCol2a.get()
        valor1 = self.listaCol4a.get()
        quant1 = self.listaCol3a.get()
        total1 = self.listaCol5a.get()
        self.conecta_Glac()
        self.listaServProd.delete(*self.listaServProd.get_children())
        lista = self.cursor.execute("""
            SELECT ordem_item, desc_item, cod_item, valor, quant, total 
            FROM orcamento2 WHERE id_orc2 = '%s' """ % id_orc)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServProd.insert("", END, values=row)
        self.desconecta_Glac()
    def altera_itens_orc_quant2(self):
        valor = self.listaCol3a.get()
        quant = self.listaCol4a.get()
        total = self.listaCol5a.get()
        valor = float(valor)
        quant = float(quant)
        self.listaCol5a.delete('0', 'end')
        soma = valor * quant
        soma = float(f'{soma:>8.2f}')
        self.listaCol5a.insert(END, soma)
    def total_orc(self):
        self.entradatotal.delete('0', 'end')
        id_orc = self.listaNumOrc.get()
        totalizador = self.entradatotal.get()

        if id_orc == '':
            msg = 'Não é possivel calcular o Valor Total se nenhum '
            msg+= 'Orçamento ou Ordem de Serviço estiver selecionada.'
            messagebox.showerror("GLAC ", msg)
        else:
            self.conecta_Glac()
            self.cursor.execute("""SELECT SUM(total) FROM orcamento2 
                WHERE id_orc2 = '%s'""" % id_orc)
            buscaNumItem = self.cursor.fetchall()
            for i in buscaNumItem:
                i = str(i)
                i = i.replace('(', '')
                i = i.replace(')', '')
                i = i.replace("'", "")
                i = i.replace(",", "h")
                i = i.replace("h", "")
                i = i.replace("R$", "")
                i = float(i)
                self.entradatotal.insert(END, self.moedaTotaliza(i))
                print(i)

            self.desconecta_Glac()
    def abre_orc(self):
        self.listaNumOrc.delete('0', 'end')
        id_orc1 = self.listaNumOrc.get()
        numeroorcamento = self.listaNumOrc.get()
        cliente_orc = self.entradaCod_cli.get()
        placa_orc = self.placa.get()
        dia = self.entradaDataorc.get()
        mes = self.entradaDataorc2.get()
        ano = self.entradaDataorc3.get()
        descp1 = self.area1.get()
        descp2 = self.area2.get()
        descp3 = self.area3.get()
        descp4 = self.area4.get()
        totalizador = self.entradatotal.get()
        km = self.entradaObs.get()
        tecnico = self.entradaTecnico.get()
        tipoOrc = self.Tipvar.get()
        comp1 = self.listInicio.get()
        comp2 = self.listFim.get()

        self.conecta_Glac()

        self.cursor.execute("""
    			INSERT INTO orcamento1 ( cliente_orc, placa_orc, descp1, descp2, 
    			    descp3, descp4, dia, mes, ano, tecnico, totalizador, tipoOrc, 
    			    km, comp1, comp2)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (cliente_orc, placa_orc, descp1, descp2, descp3, descp4,
                        dia, mes, ano, tecnico, totalizador, tipoOrc, km, comp1,
                        comp2))
        self.conn.commit()

        numeroorc = self.cursor

        numeroorc.execute("""SELECT MAX(id_orc1) FROM orcamento1""")
        buscanomecli = self.cursor.fetchall()
        for i in buscanomecli:
            self.listaNumOrc.insert(0, i)

        # variaveis orcamento2
        id_orc2 = self.listaNumOrc.get()
        cod_item1 = self.codServ1.get()
        desc_item1 = self.listaCol2a.get()

        ###
        valor1 = self.listaCol4a.get()
        quant1 = self.listaCol3a.get()
        total1 = self.listaCol5a.get()

        ################
        # Vistoria variaveis
        codVist = self.listaNumOrc.get()
        tanque = self.are1.get()
        odometro = self.are2.get()
        radio = self.are3.get()
        calota = self.are4.get()
        triangulo = self.are5.get()
        macaco = self.are6.get()
        estepe = self.are7.get()
        obs1 = self.are8.get()
        obs2 = self.are9.get()

        self.cursor.execute("""
    			INSERT INTO vistoria ( cod, vist1, vist2, vist3, vist4, vist5, 
    			    vist6, vist7, vist8, vist9)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (codVist, tanque, radio, odometro, calota, triangulo,
                        macaco, estepe, obs1, obs2))
        self.conn.commit()

        self.desconecta_Glac()

        self.total_orc()

        msg = "Orçamento gravado com sucesso.\n "
        msg += ""
        messagebox.showinfo("GLAC - Orçamento", msg)
    def altera_orc(self):
        id_orc1 = self.listaNumOrc.get()
        cliente_orc = self.entradaCod_cli.get()
        placa_orc = self.placa.get()
        dia = self.entradaDataorc.get()
        mes = self.entradaDataorc2.get()
        ano = self.entradaDataorc3.get()
        descp1 = self.area1.get()
        descp2 = self.area2.get()
        descp3 = self.area3.get()
        descp4 = self.area4.get()
        totalizador = self.entradatotal.get()
        km = self.entradaObs.get()
        tecnico = self.entradaTecnico.get()
        tipoOrc = self.Tipvar.get()
        comp1 = self.listInicio.get()
        comp2 = self.listFim.get()

        self.conecta_Glac()

        self.cursor.execute("""
    			UPDATE orcamento1 SET id_orc1 = ?, cliente_orc = ?, placa_orc = ?, dia = ?,
    			mes = ?, ano = ?, descp1 = ?, descp2 = ?, descp3 = ?, descp4 = ?, totalizador = ?, km = ?,
    			tecnico = ?, tipoOrc = ? , comp1 = ?, comp2 = ? WHERE id_orc1 = ?""",
                       (id_orc1, cliente_orc, placa_orc, dia, mes, ano, descp1, descp2, descp3,
                        descp4, totalizador, km, tecnico, tipoOrc, comp1, comp2, id_orc1))
        self.conn.commit()


        ################
        # Vistoria variaveis
        cod = self.listaNumOrc.get()
        tanque = self.are1.get()
        odometro = self.are2.get()
        radio = self.are3.get()
        calota = self.are4.get()
        triangulo = self.are5.get()
        macaco = self.are6.get()
        estepe = self.are7.get()
        obs1 = self.are8.get()
        obs2 = self.are9.get()

        self.cursor.execute("""
    			UPDATE vistoria SET vist1 = ?, vist2 = ?, vist3 = ?, vist4 = ?, vist5 = ?,
    			vist6 = ? , vist7 = ?, vist8 = ?, vist9 = ? WHERE cod = ? """,
                       (tanque, radio, odometro, calota, triangulo, macaco, estepe, obs1, obs2, cod))
        self.conn.commit()

        self.desconecta_Glac()
        self.total_orc()

        msg = "Alterações realizadas com sucesso.\n "
        msg += ""
        messagebox.showinfo("GLAC - Orçamento", msg)
    def buscanomeorc(self):
        self.listaNomeO.insert(END, '%')
        self.listaServ.delete((*self.listaServ.get_children()))

        nomeO = self.listaNomeO.get()

        self.conecta_Glac()

        nom = self.cursor

        nom.execute(
            """SELECT id_orc1, nome ,dia , mes , ano, placa_orc, orcamento1.tipoOrc FROM orcamento1, clientes WHERE  cod_cli = cliente_orc AND nome LIKE '%s' ORDER BY id_orc1 DESC""" % nomeO)
        buscanomeO = self.cursor.fetchall()
        for row in buscanomeO:
            self.listaServ.insert("", END, values=row)

        self.listaNomeO.delete(0, END)

        self.desconecta_Glac()
    def buscaplacaorc(self):
        self.listaPlaca.insert(END, '%')
        self.listaServ.delete(*self.listaServ.get_children())

        placaO = self.listaPlaca.get()
        self.conecta_Glac()

        plac = self.cursor

        plac.execute(
            """SELECT id_orc1, nome, dia , mes , ano, placa_orc, orcamento1.tipoOrc FROM orcamento1, clientes WHERE  cod_cli = cliente_orc AND placa_orc LIKE '%s'""" % placaO)
        buscaplac = self.cursor.fetchall()
        for row in buscaplac:
            self.listaServ.insert("", END, values=row)

        self.listaPlaca.delete(0, END)

        self.desconecta_Glac()
    def carrega_orc(self, event):
        self.limpa_cliente()
        self.entradaDataorc.delete('0', 'end')
        self.entradaDataorc2.delete('0', 'end')
        self.entradaDataorc3.delete('0', 'end')
        self.entradatotal.delete('0', 'end')
        self.listaNumOrc.delete('0', 'end')
        self.entradaTecnico.delete('0', 'end')

        self.listaServ.selection()

        self.conecta_Glac()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.listaServ.item(n,
                'values')
            self.listaNumOrc.insert(0, col1)

        id_orc = self.listaNumOrc.get()

        nomecur = self.cursor

        nomecur.execute("SELECT cliente_orc FROM orcamento1 "
                        "WHERE id_orc1 = '%s'" % id_orc)
        consultanome = self.cursor.fetchall()
        for i in consultanome:
            self.entradaCod_cli.insert(0, i)

        self.desconecta_Glac()
        self.carrega_cliente()
        self.conecta_Glac()

        self.entradaCod_aut.delete('0', 'end')

        nomeplaca = self.cursor

        nomeplaca.execute("SELECT placa_orc FROM orcamento1 "
                          "WHERE id_orc1 = '%s'" % id_orc)
        consultaplaca = self.cursor.fetchall()
        for i in consultaplaca:
            self.placa.insert(0, i)

        nomedescp1 = self.cursor

        nomedescp1.execute("SELECT descp1 FROM orcamento1 "
                           "WHERE id_orc1 = '%s'" % id_orc)
        consultap1 = self.cursor.fetchall()
        for i in consultap1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.area1.insert(0, i)

        nomedescp2 = self.cursor

        nomedescp2.execute("SELECT descp2 FROM orcamento1 "
                           "WHERE id_orc1 = '%s'" % id_orc)
        consultap2 = self.cursor.fetchall()
        for i in consultap2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.area2.insert(0, i)

        nomedescp3 = self.cursor

        nomedescp3.execute("SELECT descp3 FROM orcamento1 "
                           "WHERE id_orc1 = '%s'" % id_orc)
        consultap3 = self.cursor.fetchall()
        for i in consultap3:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.area3.insert(0, i)

        nomedescp4 = self.cursor

        nomedescp4.execute("SELECT descp4 FROM orcamento1 "
                           "WHERE id_orc1 = '%s'" % id_orc)
        consultap4 = self.cursor.fetchall()
        for i in consultap4:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.area4.insert(0, i)

        self.entradaDataorc.delete('0', 'end')
        nomedia = self.cursor

        nomedia.execute("SELECT dia FROM orcamento1 "
                        "WHERE id_orc1 = '%s'" % id_orc)
        consultadia = self.cursor.fetchall()
        for i in consultadia:
            self.entradaDataorc.insert(0, i)

        self.entradaDataorc2.delete('0', 'end')
        nomemes = self.cursor

        nomemes.execute("SELECT mes FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultames = self.cursor.fetchall()
        for i in consultames:
            self.entradaDataorc2.insert(0, i)

        self.entradaDataorc3.delete('0', 'end')
        nomeano = self.cursor

        nomeano.execute("SELECT ano FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultaano = self.cursor.fetchall()
        for i in consultaano:
            self.entradaDataorc3.insert(0, i)

        nometotal = self.cursor

        nometotal.execute("SELECT totalizador FROM orcamento1 "
                          "WHERE id_orc1 = '%s'" % id_orc)
        consultatotal = self.cursor.fetchall()
        for i in consultatotal:
            self.entradatotal.insert(0, i)

        nomekm = self.cursor

        nomekm.execute("SELECT km FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultakm = self.cursor.fetchall()
        for i in consultakm:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaObs.insert(0, i)

        self.cursor.execute("SELECT comp1 FROM orcamento1 "
                            "WHERE id_orc1 = '%s'" % id_orc)
        consultacomp1 = self.cursor.fetchall()
        for i in consultacomp1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listInicio.insert(0, i)

        self.cursor.execute("SELECT comp2 FROM orcamento1 "
                            "WHERE id_orc1 = '%s'" % id_orc)
        consultacomp2 = self.cursor.fetchall()
        for i in consultacomp2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listFim.insert(0, i)
        ##################################################

        placa = self.placa.get()

        nomeaut = self.cursor

        nomeaut.execute(
            "SELECT UPPER(veiculo) FROM frota WHERE placa = '%s'" % placa)
        consultaautomovel = self.cursor.fetchall()
        for i in consultaautomovel:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listAut.insert(0, i)

        nomeano = self.cursor
        nomeano.execute("SELECT ano FROM frota WHERE placa = '%s'" % placa)
        consultaano = self.cursor.fetchall()
        for i in consultaano:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listAno.insert(0, i)

        nomemarca = self.cursor
        nomemarca.execute(
            "SELECT UPPER(montadora) FROM frota WHERE placa = '%s'" % placa)
        consultamarca = self.cursor.fetchall()
        for i in consultamarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listMarca.insert(0, i)

        nomecomb = self.cursor
        nomecomb.execute("SELECT UPPER(combust) FROM frota "
                         "WHERE placa = '%s'" % placa)
        consultacomb = self.cursor.fetchall()
        for i in consultacomb:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listCombustivel.insert(0, i)

        nomecor = self.cursor
        nomecor.execute("SELECT UPPER(cor) FROM frota WHERE placa = '%s'" % placa)
        consultacor = self.cursor.fetchall()
        for i in consultacor:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listCor.insert(0, i)

        #############################################

        self.listaServProd.delete(*self.listaServProd.get_children())
        lista = self.cursor.execute("""SELECT ordem_item, desc_item, cod_item, valor, quant, total FROM orcamento2
                    WHERE id_orc2 = '%s' """ % id_orc)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServProd.insert("", 0, values=row)

        ##################################


        ##################################

        tec = self.cursor

        tec.execute("SELECT tecnico FROM orcamento1 WHERE id_orc1 = '%s' " % id_orc)
        tecd = self.cursor.fetchall()
        for i in tecd:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaTecnico.insert(0, i)

        orcos = self.cursor
        orcos.execute("Select tipoOrc From orcamento1 "
                      "Where id_orc1 = '%s' " % id_orc)
        orcos1 = self.cursor.fetchall()
        for i in orcos1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.Tipvar.set(i)

        ################
        # Vistoria variaveis
        codVist = self.listaNumOrc.get()
        tanque = self.are1.get()
        odometro = self.are2.get()
        radio = self.are3.get()
        calota = self.are4.get()
        triangulo = self.are5.get()
        macaco = self.are6.get()
        estepe = self.are7.get()
        obs1 = self.are8.get()
        obs2 = self.are9.get()

        self.cursor.execute("SELECT vist1 FROM vistoria "
                            "WHERE cod = '%s' " % codVist)
        codVisto = self.cursor.fetchall()
        for i in codVisto:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are1.insert(0, i)

        self.cursor.execute("SELECT vist2 FROM vistoria "
                            "WHERE cod = '%s' " % codVist)
        codR = self.cursor.fetchall()
        for i in codR:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are3.insert(0, i)

        self.cursor.execute("SELECT vist3 FROM vistoria "
                            "WHERE cod = '%s' " % codVist)
        codO = self.cursor.fetchall()
        for i in codO:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are2.insert(0, i)

        self.cursor.execute("SELECT vist4 FROM vistoria "
                            "WHERE cod = '%s' " % codVist)
        codCalota = self.cursor.fetchall()
        for i in codCalota:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are4.insert(0, i)

        self.cursor.execute("SELECT vist5 FROM vistoria "
                            "WHERE cod = '%s' " % codVist)
        codTri = self.cursor.fetchall()
        for i in codTri:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are5.insert(0, i)

        self.cursor.execute("SELECT vist6 FROM vistoria "
                            "WHERE cod = '%s' " % codVist)
        cod6 = self.cursor.fetchall()
        for i in cod6:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are6.insert(0, i)

        self.cursor.execute("SELECT vist7 FROM vistoria "
                            "WHERE cod = '%s' " % codVist)
        cod7 = self.cursor.fetchall()
        for i in cod7:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are7.insert(0, i)

        self.cursor.execute("SELECT vist8 FROM vistoria "
                            "WHERE cod = '%s' " % codVist)
        cod8 = self.cursor.fetchall()
        for i in cod8:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are8.insert(0, i)

        self.cursor.execute("SELECT vist9 FROM vistoria "
                            "WHERE cod = '%s' " % codVist)
        cod9 = self.cursor.fetchall()
        for i in cod9:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are9.insert(0, i)

        self.listaOrc.destroy()
        self.desconecta_Glac()

        self.total_orc()

        def carrega_orc_a(event):
            carrega_orc()
    def OnDoubleClick(self, event):
        self.limpa_cliente()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5 = listaServ.item(n, 'values')
            self.entradan.insert(END, col1)

        self.carrega_orc()
    def backup(self):
        try:
            shutil.copyfile("c:\glacx\glac.db", "c:\glacbkp\copiaGlacX.db")
            msg = "Backup salvo em c:\glacbkp\ \n" \
                 "Copie e salve em local seguro. ;) "
            msg += ""
            messagebox.showinfo("GLACX", msg)
        except:
            msg = "Copia não realizada, crie a pasta c:\glacbkp \n" \
                  "antes de realizar o backup"
            messagebox.showinfo("GLACX", msg)
    def busca_serv(self):
        # self.listaServ1.delete(0, END)
        self.listaServ1.delete(*self.listaServ1.get_children())
        self.listaServicos1.insert(END, '%')

        self.conecta_Glac()

        servprod = self.listaServicos1.get()

        servico12 = self.cursor

        servico12.execute("""SELECT cod_sp, servprod, tiposerv, hor, descricao, id_marcaprod, sistemaserv, valor * hor
    	FROM servprod WHERE servprod LIKE '%s' """ % servprod)
        buscaservico12 = self.cursor.fetchall()
        for i in buscaservico12:
            self.listaServ1.insert("", END, values=i)

        self.listaServicos1.delete(0, END)

        self.desconecta_Glac()
    def OnVsb_S1F(self, *args):
        self.listaServ1F.yview(*args)
    def busca_servF(self):
        # self.listaServ1.delete(0, END)
        self.listaServ1F.delete(*self.listaServ1F.get_children())
        self.listaServicos1F.insert(END, '%')

        self.conecta_Glac()

        servprodF = self.listaServicos1F.get()

        servico12F = self.cursor

        servico12F.execute("""SELECT cod_falha, falha, falha2 FROM codfalha WHERE falha LIKE '%s' """ % servprodF)
        buscaservico12F = self.cursor.fetchall()
        for i in buscaservico12F:
            self.listaServ1F.insert("", END, values=i)

        self.listaServicos1F.delete(0, END)
        self.desconecta_Glac()
    def PaginaRf(self):
        webbrowser.open("https://www.facebook.com/rfzorzi/")
    def buscaCli(self):
        self.conecta_Glac()
        self.EntryCliente2.insert(END, '%')
        nome = self.EntryCliente2.get()
        nomecod = self.cursor
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
            SELECT cod_cli, nome FROM clientes WHERE nome LIKE '%s' 
            """ % nome)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
        self.EntryCliente2.delete(0, END)
        self.desconecta_Glac()
    def carrega_cliente2C(self, event):
        self.limpa_clienteC()

        pos = int(self.listaServ2.curselection()[0])
        cod_cli = self.listaServ2.get(pos)

        self.cursor.execute("SELECT cod_cli FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacod = cursor.fetchall()
        for i in consultacod:
            self.entradaCod_clicC.insert(END, i)

        self.carrega_clienteC()

    def busca_serv_veic(self):
        # self.listaServ1.delete(0, END)
        self.listaServ1.delete(*self.listaServ1.get_children())
        self.listaServicos1.insert(END, '%')

        servprod = self.listaServicos1.get()

        self.conecta_Glac()

        servico12 = self.cursor

        servico12.execute("""SELECT cod_sp, servprod, tiposerv, hor, descricao, id_marcaprod, sistemaserv, valor * hor
    	FROM servprod WHERE id_marcaprod LIKE '%s' """ % servprod)
        buscaservico12 = self.cursor.fetchall()
        for i in buscaservico12:
            self.listaServ1.insert("", END, values=i)

        self.listaServicos1.delete(0, END)

        self.desconecta_Glac()
    def OnVsb(self, *args):
        self.listaServ.yview(*args)
    def OnVsb_S1(self, *args):
        self.listaServ1.yview(*args)
    def OnVsb_Orc(self, *args):
        self.listaServ.yview(*args)
    def totalbotao(self):
        def moedaTotal1(total1=0, moeda='R$'):
            return f'{moeda}{total1:>8.2f}'.replace('.', ',')
        quant1 = self.listaCol3a.get()
        quant1 = float(quant1)
        valor1 = self.listaCol4a.get()
        valor1 = float(valor1)
        total1 = quant1 * valor1
        total1 = float(f'{moeda}{total1:>8.2f}')
        self.listaCol5a.delete(0, END)
        self.listaCol5a.insert(END, total1)

        self.entradatotal.delete(0, END)
        self.totalsimples = float(total1 )
        self.entradatotal.insert(END, self.moedaTotalizador(total1 ))
    def add_servico1bind(self, event):
        self.codServ1.delete(0, END)
        self.listaCol2a.delete(0, END)
        self.listaCol4a.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, \
            col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ1.insert(END, col1)

        self.add_servico1()
        self.listaServP1.destroy()
