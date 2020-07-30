from tkinter import *
from tkinter import messagebox
import webbrowser

class SegundoFrame:
    def limpa_cliente(self):
        self.entradaCod_cli.delete('0', 'end')
        self.listNome.delete('0', 'end')
        self.listEndereco.delete('0', 'end')
        self.listBairro.delete('0', 'end')
        self.listMunicipio.delete('0', 'end')
        self.listCpf.delete('0', 'end')
        self.listFone.delete('0', 'end')
        self.listUf.delete('0', 'end')
        self.listObs.delete('0', 'end')
        self.entradaCod_aut.delete('0', 'end')
        self.listAut.delete('0', 'end')
        self.listAno.delete('0', 'end')
        self.listMarca.delete('0', 'end')
        self.listCombustivel.delete('0', 'end')
        self.listCor.delete('0', 'end')
        self.placa.delete('0', 'end')
        self.entradaObs.delete('0', 'end')
        self.area1.delete('0', 'end')
        self.area2.delete('0', 'end')
        self.area3.delete('0', 'end')
        self.area4.delete('0', 'end')
        self.entradatotal.delete('0', 'end')
        self.listInicio.delete('0', 'end')
        self.listFim.delete('0', 'end')

        self.codServ1.delete('0', 'end')

        self.listaCol2a.delete('0', 'end')
        self.listaCol3a.delete('0', 'end')
        self.listaCol3a.insert(0, '1')
        self.listaCol4a.delete('0', 'end')
        self.listaCol4a.insert(0, 'R$ 0,00')
        self.listaCol5a.delete('0', 'end')
        self.listaCol5a.insert(0, 'R$ 0,00')

        self.listaNumOrc.delete('0', 'end')
        self.are1.delete('0', 'end')
        self.are2.delete('0', 'end')
        self.are3.delete('0', 'end')
        self.are4.delete('0', 'end')
        self.are5.delete('0', 'end')
        self.are6.delete('0', 'end')
        self.are7.delete('0', 'end')
        self.are8.delete('0', 'end')
        self.are9.delete('0', 'end')


        self.listaServProd.delete(*self.listaServProd.get_children())
    def carrega_automovel(self, event):
        self.listAut.delete('0', 'end')
        self.listAno.delete('0', 'end')
        self.listMarca.delete('0', 'end')
        self.listCombustivel.delete('0', 'end')
        self.listCor.delete('0', 'end')
        self.listObs.delete('0', 'end')
        self.placa.delete('0', 'end')

        self.conecta_Glac()

        pos = int(self.entradaCod_aut.curselection()[0])
        placa = self.entradaCod_aut.get(pos)

        nomeplac = self.cursor
        nomeplac.execute("SELECT placa FROM frota WHERE placa = '%s'" % placa)
        consultaplac = self.cursor.fetchall()
        for i in consultaplac:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.placa.insert(0, i)

        nomeaut = self.cursor
        nomeaut.execute("SELECT UPPER(veiculo) FROM frota WHERE placa = '%s'" % placa)
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
        nomecomb.execute("SELECT UPPER(combust) FROM frota WHERE placa = '%s'" % placa)
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

        self.desconecta_Glac()

        def carrega_automovel_a(event):
            carrega_automovel()
    def carrega_cliente(self):
        self.conecta_Glac()
        cod_cli = self.entradaCod_cli.get()
        nomecur = self.cursor
        nomecur.execute("SELECT UPPER(nome) FROM clientes "
                        "WHERE cod_cli = '%s'" % cod_cli)
        consultanome = self.cursor.fetchall()
        for i in consultanome:
            i = str(i)
            i = i.replace('(', '')
            i = i.replace(')', '')
            i = i.replace("'", "")
            i = i.replace(',', '')
            self.listNome.insert(END, i)
            print(i)

        nomeend = self.cursor
        nomeend.execute("""SELECT UPPER(endereco), "Nº", numcasa
            FROM clientes WHERE cod_cli = '%s' """ % cod_cli)
        consultaend = self.cursor.fetchall()
        for i in consultaend:
            i = str(i)
            i = i.replace('(', '')
            i = i.replace(')', '')
            i = i.replace("'", "")
            i = i.replace(',', '')
            self.listEndereco.insert(END, i)
            print(i)

        nomebairro = self.cursor
        nomebairro.execute("SELECT UPPER(bairro) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultabairro = self.cursor.fetchall()
        for i in consultabairro:
            i = str(i)
            i = i.replace('(', '')
            i = i.replace(')', '')
            i = i.replace("'", "")
            i = i.replace(',', '')
            self.listBairro.insert(END, i)
            print(i)

        nomemunicipio = self.cursor
        nomemunicipio.execute("SELECT UPPER(municipio) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultamunicipio = self.cursor.fetchall()
        for i in consultamunicipio:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listMunicipio.insert(END, i)
            print(i)

        nomecpf = self.cursor
        nomecpf.execute("SELECT cpf FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacpf = self.cursor.fetchall()
        for i in consultacpf:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listCpf.insert(END, i)
            print(i)

        nomefone = self.cursor
        nomefone.execute("SELECT fone1ddd, fone1 FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone = self.cursor.fetchall()
        for i in consultafone:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listFone.insert(END, i)
            print(i)

        nomeuf = self.cursor
        nomeuf.execute("SELECT UPPER(uf) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultauf = self.cursor.fetchall()
        for i in consultauf:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listUf.insert(END, i)
            print(i)

        nomeobs = self.cursor
        nomeobs.execute("SELECT obs FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultaobs = self.cursor.fetchall()
        for i in consultaobs:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listObs.insert(END, i)
            print(i)

        pla = self.cursor
        pla.execute("SELECT placa FROM frota, clientes "
                    "WHERE idcliente = cod_cli and cod_cli = '%s'" % cod_cli)
        consultapla = self.cursor.fetchall()
        for i in consultapla:
            self.entradaCod_aut.insert(END, i)

        self.desconecta_Glac()

        def carrega_cliente_a(event):
            self.carrega_cliente()
    def carrega_cliente2(self, event):
        self.limpa_cliente()
        #### Variaveis da função
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2 = self.listaServ.item(n, 'values')
            self.entradaCod_cli.insert(0, col1)

        self.carrega_cliente()
        self.listacliente.destroy()

        def carrega_cliente2_a(event):
            self.carrega_cliente2()

