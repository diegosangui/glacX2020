from funcs.modulos import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.labelStyle import LabelGlac
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *
from funcs.backCads.backCadCli import *

class Clientes(CadCli):
    def cadcli(self):
        self.telaCliente()
        self.molduraCliente()
        self.WidgetsClientes()
        self.listaClientes()
        self.WidgetsVeiculos()
        self.janelaCli.mainloop()
    def telaCliente(self):
        self.janelaCli = Toplevel(self.janela)
        self.janelaCli.title("Cadastro de Clientes")
        self.janelaCli.configure(background='#1e3743')
        self.janelaCli.focus_force()
        self.janelaCli.geometry("800x600")
        self.janelaCli.resizable(TRUE, TRUE)
        self.janelaCli.minsize(width=780, height=450)
        self.janelaCli.transient(self.janela)
        self.janelaCli.focus_force()
        self.janelaCli.grab_set()

        self.background_label = Label(self.janelaCli,
            image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)
    def molduraCliente(self):
        self.titulo_cliente = LabelGlac(self.janelaCli)
        self.titulo_cliente.configure(text=self.m_Clientes)
        self.titulo_cliente.place(relx=0.01, rely=0.04,
            relwidth=0.2, relheight=0.03)

        self.tituloListaClientes = LabelGlac(self.janelaCli)
        self.tituloListaClientes.configure(text='Lista de Clientes')
        self.tituloListaClientes.place(relx=0.495, rely=0.04,
            relwidth=0.3, relheight=0.03)

        self.frameCadastroCliente = GradientFrame(self.janelaCli)
        self.frameCadastroCliente.place(relx=0.01, rely=0.07,
            relwidth=0.48, relheight=0.46)

        self.frameListaClientes = GradientFrame(self.janelaCli)
        self.frameListaClientes.place(relx=0.495, rely=0.07,
            relwidth=0.49, relheight=0.46)

        self.frameVeiculos = GradientFrame(self.janelaCli)
        self.frameVeiculos.place(relx=0.01, rely=0.58,
            relwidth=0.97, relheight=0.4)

        self.tituloVeiculos = LabelGlac(self.janelaCli)
        self.tituloVeiculos.configure(text=self.m_Automoveis)
        self.tituloVeiculos.place(relx=0.01, rely=0.55,
            relwidth=0.2, relheight=0.028)
    def WidgetsClientes(self):
        #'Label Codigo'
        self.codPeLabel = LabelGlac(self.janelaCli)
        self.codPeLabel.configure(text=self.m_Codigo)
        self.codPeLabel.place(relx=0.02, rely=0.095,
            width=60, height=20)

        #'Entry Código'
        self.codPeEntry = EntPlaceHold(self.janelaCli, '')
        self.codPeEntry.configure(
            validate="key", validatecommand=self.vcmd8)
        self.codPeEntry.place(relx=0.02, rely=0.122,
            relwidth=0.05, relheight=0.026)

        #'Label Data de Nascimento'
        self.nascPeLabel = LabelGlac(self.janelaCli)
        self.nascPeLabel.configure(text=self.m_Nasc)
        self.nascPeLabel.place(relx=0.39, rely=0.15,
            relwidth=0.07, relheight=0.02)

        #'Entry Dia'
        self.nascDiaPeEntry = Entry(self.janelaCli)
        self.nascDiaPeEntry.configure(
            validate="key", validatecommand=self.vcmd2)
        self.nascDiaPeEntry.place(relx=0.38, rely=0.17,
            relwidth=0.03, relheight=0.03)

        #'Entry Mês'
        self.nascMesPeEntry = Entry(self.janelaCli)
        self.nascMesPeEntry.configure(validate="key",
                                      validatecommand=self.vcmd2)
        self.nascMesPeEntry.place(relx=0.41, rely=0.17,
            relwidth=0.03, relheight=0.03)

        #'Entry Ano'
        self.nascAnoPeEntry = Entry(self.janelaCli)
        self.nascAnoPeEntry.configure(validate="key",
                                      validatecommand=self.vcmd4)
        self.nascAnoPeEntry.place(relx=0.44, rely=0.17,
            relwidth=0.04, relheight=0.03)

        #'Label Nome do Cliente'
        self.nomePeLabel = LabelGlac(self.janelaCli)
        self.nomePeLabel.configure(
            text=self.m_Nome, font=('Arial', '8', 'bold'))
        self.nomePeLabel.place(relx=0.02, rely=0.15,
            relwidth=0.05, relheight=0.02)

        #'Entry Nome Do Cliente'
        self.nomePeEntry = Entry(self.janelaCli)
        self.nomePeEntry.configure(font=('Arial', '8', 'bold'))
        self.nomePeEntry.place(relx=0.02, rely=0.17,
            relwidth=0.35, relheight=0.03)

        #'Label Logradouro'
        self.logradPeLabel = LabelGlac(self.janelaCli)
        self.logradPeLabel.configure(font=('Verdana', '8', 'bold'),
            text=self.m_Endereco)
        self.logradPeLabel.place(relx=0.02, rely=0.2,
            relwidth=0.08, relheight=0.02)

        #'Entry Logradouro'
        self.logradPeEntry = Entry(self.janelaCli)
        self.logradPeEntry.configure(font=('Arial', '8', 'bold'))
        self.logradPeEntry.place(relx=0.02, rely=0.22,
            relwidth=0.38, relheight=0.03)

        #'Label Numero'
        self.numPeLabel = LabelGlac(self.janelaCli)
        self.numPeLabel.configure(font=('Verdana', '8', 'bold'),
            text=self.m_Numero)
        self.numPeLabel.place(relx=0.405, rely=0.2,
            relwidth=0.07, relheight=0.02)

        #'Entry Numero'
        self.numPeEntry = Entry(self.janelaCli)
        self.numPeEntry.configure(font=('Arial', '8', 'bold'))
        self.numPeEntry.place(relx=0.41, rely=0.22,
            relwidth=0.06, relheight=0.03)

        #'Label Complemento'
        self.complemPeLabel = LabelGlac(self.janelaCli)
        self.complemPeLabel.configure(font=('Verdana', '8', 'bold'),
            text=self.m_Complemento)
        self.complemPeLabel.place(relx=0.02, rely=0.25,
            relwidth=0.12, relheight=0.02)

        #'Entry Complemento'
        self.complemPeEntry = Entry(self.janelaCli)
        self.complemPeEntry.configure(font=('Arial', '8', 'bold'))
        self.complemPeEntry.place(relx=0.02, rely=0.27,
            relwidth=0.22, relheight=0.03)

        #'Label Bairro'
        self.bairroPeLabel = LabelGlac(self.janelaCli)
        self.bairroPeLabel.configure(font=('Verdana', '8', 'bold'),
            text=self.m_Bairro)
        self.bairroPeLabel.place(relx=0.25, rely=0.25,
            relwidth=0.06, relheight=0.02)

        #'Entry Bairro'
        self.bairroPeEntry = Entry(self.janelaCli)
        self.bairroPeEntry.configure(font=('Arial', '8', 'bold'))
        self.bairroPeEntry.place(relx=0.25, rely=0.27,
            relwidth=0.22, relheight=0.03)

        #'Label Municipio'
        self.cidadePeLabel = LabelGlac(self.janelaCli)
        self.cidadePeLabel.configure(font=('Verdana', '8', 'bold'),
            text=self.m_Cidade)
        self.cidadePeLabel.place(relx=0.02, rely=0.3,
            relwidth=0.06, relheight=0.02)

        #'Entry Municipio'
        self.cidadePeEntry = Entry(self.janelaCli)
        self.cidadePeEntry.configure(font=('Arial', '8', 'bold'))
        self.cidadePeEntry.place(relx=0.02, rely=0.32,
            relwidth=0.41, relheight=0.03)

        #'Label UF'
        self.ufPeLabel = LabelGlac(self.janelaCli)
        self.ufPeLabel.configure(font=('Verdana', '8', 'bold'),
            text=self.m_Uf)
        self.ufPeLabel.place(relx=0.44, rely=0.3,
            relwidth=0.03, relheight=0.02)

        #'Entry UF'
        self.ufPeEntry = Entry(self.janelaCli)
        self.ufPeEntry.configure(font=('Arial', '8', 'bold'))
        self.ufPeEntry.place(relx=0.44, rely=0.32,
            relwidth=0.03, relheight=0.03)

        #'Label Fone'
        self.fone1Pelabel = LabelGlac(self.janelaCli)
        self.fone1Pelabel.configure(
            text='Fone 1:', font=('Verdana', '8', 'bold'))
        self.fone1Pelabel.place(relx=0.02, rely=0.35,
            relwidth=0.06, relheight=0.02)

        #'Entry Fone 1'
        self.fone1PeEntry = Entry(self.janelaCli)
        self.fone1PeEntry.configure(font=('Verdana', '8', 'bold'),
            validate="key", validatecommand=self.vcmd2)
        self.fone1PeEntry.place(relx=0.02, rely=0.37,
            relwidth=0.03, relheight=0.03)

        self.fone1PeEntry2 = Entry(self.janelaCli)
        self.fone1PeEntry2.configure(font=('Verdana', '8', 'bold'),
            validate="key", validatecommand=self.vcmd12)

        self.fone1PeEntry2.place(relx=0.06, rely=0.37,
            relwidth=0.12, relheight=0.03)

        #'Label Fone 2'
        self.fone2Pelabel = LabelGlac(self.janelaCli)
        self.fone2Pelabel.configure(font=('Verdana', '8', 'bold'),
            text='Fone 2')
        self.fone2Pelabel.place(relx=0.24, rely=0.35,
            relwidth=0.06, relheight=0.02)

        #'Entry Fone 2'
        self.fone2PeEntry = Entry(self.janelaCli)
        self.fone2PeEntry.configure(
            font=('Verdana', '8', 'bold'),
            validate="key", validatecommand=self.vcmd2)
        self.fone2PeEntry.place(relx=0.24, rely=0.37,
            relwidth=0.03, relheight=0.03)

        self.fone2PeEntry2 = Entry(self.janelaCli)
        self.fone2PeEntry2.configure(
            font=('Verdana', '8', 'bold'),
            validate="key", validatecommand=self.vcmd12)
        self.fone2PeEntry2.place(relx=0.28, rely=0.37,
            relwidth=0.12, relheight=0.03)

        #'Label Cpf'
        self.cpfPeLabel = LabelGlac(self.janelaCli)
        self.cpfPeLabel.configure(text=self.m_Cpf)
        self.cpfPeLabel.configure(font=('Verdana', '8', 'bold'))
        self.cpfPeLabel.place(relx=0.31, rely=0.4,
            relwidth=0.05, relheight=0.02)

        #'Entry CPF'
        self.cpfPeEntry = Entry(self.janelaCli)
        self.cpfPeEntry.configure(font=('Verdana', '8', 'bold'),
            validatecommand=self.vcmd12)
        self.cpfPeEntry.place(relx=0.31, rely=0.42,
            relwidth=0.16, relheight=0.03)

        #'Label CNPJ'
        self.cnpjPeLabel = LabelGlac(self.janelaCli)
        self.cnpjPeLabel.configure(text=self.m_Cnpj)
        self.cnpjPeLabel.configure(font=('Verdana', '8', 'bold'))
        self.cnpjPeLabel.place(relx=0.14, rely=0.4,
            relwidth=0.05, relheight=0.02)

        #'Entry CNPJ'
        self.cnpjPeEntry = Entry(self.janelaCli)
        self.cnpjPeEntry.configure(font=('Verdana', '8', 'bold'),
            validate="key", validatecommand=self.vcmd12)
        self.cnpjPeEntry.place(relx=0.14, rely=0.42,
            relwidth=0.16, relheight=0.03)

        #'Label RG'
        self.rgPeLabel = LabelGlac(self.janelaCli)
        self.rgPeLabel.configure(text=self.m_RG)

        #'Entry RG'
        self.rgPeEntry = Entry(self.janelaCli)

        #'Label Obs'
        self.obsPeLabel = LabelGlac(self.janelaCli)
        self.obsPeLabel.configure(font=('Verdana', '8', 'bold'),
            text = self.m_Obs)
        self.obsPeLabel.place(relx=0.02, rely=0.45,
            relwidth=0.05, relheight=0.02)

        #'Entry Obs'
        self.obsPeEntry = Entry(self.janelaCli)
        self.obsPeEntry.configure(font=('Arial', '8', 'bold'))
        self.obsPeEntry.place(relx=0.02, rely=0.47,
            relwidth=0.22, relheight=0.028)

        #'Label E-mail'
        self.emailPeLabel = LabelGlac(self.janelaCli)
        self.emailPeLabel.configure(font=('Verdana', '8', 'bold'),
            text='E-mail')
        self.emailPeLabel.place(relx=0.25, rely=0.45,
            relwidth=0.05, relheight=0.02)

        #'Entry E-mail'
        self.emailPeEntry = Entry(self.janelaCli)
        self.emailPeEntry.configure(font=('Arial', '8', 'bold'))
        self.emailPeEntry.place(relx=0.25, rely=0.47,
            relwidth=0.22, relheight=0.028)

        #'Label Inscrição Estadual'
        self.inscEstPeLabel = Label(self.janelaCli,
            text='Inscrição Estadual', bg="#49708D", fg="white")

        #'Entry Inscrição Estadual'
        self.inscEstPeEntry = Entry(self.janelaCli,
            bg=self.bg_entry)

        #'Botao Cep'
        self.cepPeBt = ButtonGlac(self.janelaCli)
        self.cepPeBt.configure(text='>>',
            command=self.cep)
        self.cepPeBt.place(relx=0.02, rely=0.42,
            relwidth=0.04, relheight=0.03)

        #'Label Cep'
        self.cepPeLabel = LabelGlac(self.janelaCli)
        self.cepPeLabel.configure(font=('Verdana', '8', 'bold'),
            text=self.m_Cep)
        self.cepPeLabel.place(relx=0.02, rely=0.4,
            relwidth=0.06, relheight=0.02)

        #'Entry Cep'
        self.cepPeEntry = Entry(self.janelaCli)
        self.cepPeEntry.configure(validate="key",
            font= ('Verdana', 8), validatecommand=self.vcmd8)
        self.cepPeEntry.place(relx=0.06, rely=0.42,
            relwidth=0.07, relheight=0.03)

        #'Botao Novo Cliente'
        self.botaoAdd = ButtonGlac(self.janelaCli)
        self.botaoAdd.configure(text=self.m_Novo,
            command=self.add_clienteC)
        self.botaoAdd.place(relx=0.25, rely=0.08,
            width=60, height=25)

        # Botao Altera dados do Cliente
        self.botaoMud = ButtonGlac(self.janelaCli)
        self.botaoMud.configure(command=self.mud_clienteC,
            text=self.m_Alterar)
        self.botaoMud.place(relx=0.33, rely=0.08,
            width=60, height=25)

        # Botao deletar dados do Cliente
        self.botaoDel = ButtonGlac(self.janelaCli)
        self.botaoDel.configure(text=self.m_Apagar,
            command=self.deletar_windowC)
        self.botaoDel.place(relx=0.41, rely=0.08,
            width=60, height=25)

        #  Botao limpa
        self.botaolimpa = ButtonGlac(self.janelaCli)
        self.botaolimpa.configure(text=self.m_Limpar,
            command=self.limpa_clienteC)
        self.botaolimpa.place(relx=0.17, rely=0.08,
            width=60, height=25)

        #  Botao busca Cabeça
        self.botaobusca = ButtonGlac(self.janelaCli)
        self.botaobusca.configure(bitmap='questhead',
            font=('Verdana', '8', 'bold'), command=self.busca_clienteC)
        self.botaobusca.place(relx=0.11, rely=0.08, width=35)
    def listaClientes(self):
        self.barracliente = Scrollbar(self.janelaCli,
            orient='vertical', command=self.OnVsbC)
        self.listaServ = ttk.Treeview(self.janelaCli,
            height=6, yscrollcommand=self.barracliente.set,
            column=("col1", "col2", "col3", "col4"))

        self.listaServ.heading("#0", text="")
        self.listaServ.column("#0", width=1)
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.column("#1", width=40)
        self.listaServ.heading("#2", text=self.m_Nome)
        self.listaServ.column("#2", width=185)
        self.listaServ.heading("#3", text='')
        self.listaServ.column("#3", width=30)
        self.listaServ.heading("#4", text=self.m_Fone)
        self.listaServ.column("#4", width=105)

        self.listaServ.place(relx=0.5, rely=0.09,
                             relwidth=0.465, relheight=0.42)
        self.listaServ.configure(yscroll=self.barracliente.set)
        self.barracliente.place(relx=0.965, rely=0.09,
                                relwidth=0.015, relheight=0.42)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickC)

        self.conecta_Glac()
        self.lista1 = self.cursor.execute(
            """SELECT  cod_cli, nome, fone1ddd, fone1
            FROM clientes  ORDER BY nome ASC; """)
        for i in self.lista1:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()
    def WidgetsVeiculos(self):
        self.entradaVeiculo2 = Entry(self.janelaCli)
        self.entradaVeiculo2.configure(font=('Verdana', '8', 'bold'))

        self.entradaMontadora2 = Entry(self.janelaCli)
        self.entradaMontadora2.configure(font=('Verdana', '8', 'bold'))

        # Label Código
        self.codEquipLabel = LabelGlac(self.janelaCli)
        self.codEquipLabel.configure(text=self.m_Codigo)

        # Entry Código
        self.codEquipEntry = Entry(self.janelaCli)
        self.codEquipEntry.configure(font=('Verdana', '8', 'bold'))

        # Label Ano
        self.fabrAnoEquipLabel = LabelGlac(self.janelaCli)
        self.fabrAnoEquipLabel.configure(text=self.m_Ano,
                                         font=('Verdana', '8', 'bold'))
        # Entry Ano
        self.fabrAnoEquipEntry = Entry(self.janelaCli)
        self.fabrAnoEquipEntry.configure(font=('Verdana', '8', 'bold'))
        self.fabrAnoEquipEntry.place(relx=0.65, rely=0.63,
                                     relwidth=0.1, relheight=0.04)

        self.fabrModeloEquipLabel = LabelGlac(self.janelaCli)
        self.fabrModeloEquipLabel.configure(text=self.m_Ano)
        self.fabrAnoEquipLabel.place(relx=0.65, rely=0.59,
                                     relwidth=0.1, relheight=0.04)

        self.fabrModeloEquipEntry = Entry(self.janelaCli)
        self.fabrModeloEquipEntry.configure(font=('Verdana', '8', 'bold'))

        self.nomeEquipLabel = LabelGlac(self.janelaCli)
        self.nomeEquipLabel.configure(text=self.m_Automovel)

        self.nomeEquipEntry = Entry(self.janelaCli)
        self.nomeEquipEntry.configure(font=('Verdana', '8', 'bold'))
        self.nomeEquipEntry.place(relx=0.13, rely=0.63,
                                  relwidth=0.1, relheight=0.04)

        self.nomeIdEquipEntry = Entry(self.janelaCli)
        self.nomeIdEquipEntry.configure(font=('Verdana', '8', 'bold'))

        self.serialEquipLabel = LabelGlac(self.janelaCli)
        self.serialEquipLabel.configure(text=self.m_Placa,
                                        font=('Verdana', '7', 'bold'))
        self.serialEquipLabel.place(relx=0.02, rely=0.59,
                                    relwidth=0.1, relheight=0.04)

        self.serialEquipEntry = Entry(self.janelaCli)
        self.serialEquipEntry.configure(font=('Verdana', '8', 'bold'))
        self.serialEquipEntry.place(relx=0.02, rely=0.63,
                                    relwidth=0.1, relheight=0.04)

        self.corEquipLabel = LabelGlac(self.janelaCli)
        self.corEquipLabel.configure(text=self.m_Cor,
                                     font=('Verdana', '7', 'bold'))
        self.corEquipLabel.place(relx=0.35, rely=0.59,
                                 relwidth=0.12, relheight=0.04)

        self.corvar = StringVar(self.janelaCli)
        self.coresV = {self.m_Branco, self.m_Amarelo, self.m_Verde,
                       self.m_Bege, self.m_Azul, self.m_Laranja,
                       self.m_Vermelho, self.m_Verde, self.m_Cinza,
                       self.m_Preto, self.m_Marrom, self.m_Bordo,
                       self.m_Prata, self.m_Grafite, self.m_Dourado,
                       self.m_Outro}

        self.corvar.set(self.m_Branco)

        self.popupMenu = OptionMenu(self.janelaCli,
                                    self.corvar, *self.coresV)
        self.popupMenu.place(relx=0.35, rely=0.63,
                             relwidth=0.12, relheight=0.04)

        self.combEquipLabel = LabelGlac(self.janelaCli)
        self.combEquipLabel.configure(text=self.m_Combustivel,
                                      font=('Verdana', '7', 'bold'))
        self.combEquipLabel.place(relx=0.48, rely=0.59,
                                  relwidth=0.16, relheight=0.04)

        self.combvar = StringVar()
        self.combV = {self.m_Gasolina, self.m_Alcool, self.m_Diesel,
                      self.m_Flex, self.m_Gasolina_e_Gas, self.m_Alcool_e_Gas,
                      self.m_Flex_e_Gas}
        self.combvar.set(self.m_Gasolina)

        self.popupMenu = OptionMenu(self.janelaCli,
                                    self.combvar, *self.combV)
        self.popupMenu.place(relx=0.48, rely=0.63,
                             relwidth=0.16, relheight=0.04)

        self.marcaEquipLabel = LabelGlac(self.janelaCli)
        self.marcaEquipLabel.configure(text=self.m_Marca,
                                       font=('Verdana', '7', 'bold'))
        self.marcaEquipLabel.place(relx=0.24, rely=0.59,
                                   relwidth=0.1, relheight=0.04)

        self.marcaEquipEntry = Entry(self.janelaCli)
        self.marcaIdEquipEntry = EntPlaceHold(self.janelaCli, '')
        self.marcaEquipEntry.place(relx=0.24, rely=0.63,
                                   relwidth=0.1, relheight=0.04)

        ##### Veiculo
        self.descrVeiculo = ButtonGlac(self.janelaCli)
        self.descrVeiculo.configure(command=self.busca_autoC,
                                    text=self.m_Veiculo)
        self.descrVeiculo.place(relx=0.13, rely=0.59,
                                relwidth=0.1, relheight=0.04)

        #  Botoes automoveis
        self.botaoAdd2 = ButtonGlac(self.janelaCli)
        self.botaoAdd2.configure(text=self.m_Novo)
        self.botaoAdd2.configure(command=self.add_veiculoC)
        self.botaoAdd2.place(relx=0.9, rely=0.63, relwidth=0.07, relheight=0.04)

        self.botaoMud2 = ButtonGlac(self.janelaCli)
        self.botaoMud2.configure(text=self.m_Alterar)
        self.botaoMud2.configure(command=self.mud_autoC)
        self.botaoMud2.place(relx=0.9, rely=0.7,
                             relwidth=0.07, relheight=0.04)

        self.botaoDel2 = ButtonGlac(self.janelaCli)
        self.botaoDel2.configure(text=self.m_Apagar,
                                command=self.deletar_windowPlacaC)
        self.botaoDel2.place(relx=0.9, rely=0.77,
                            relwidth=0.07, relheight=0.04)

        self.listaPlaca = ttk.Treeview(self.janelaCli, height=5,
            column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaPlaca.heading("#0", text="")
        self.listaPlaca.column("#0", width=0)
        self.listaPlaca.heading("#1", text=self.m_Placa)
        self.listaPlaca.column("#1", width=80)
        self.listaPlaca.heading("#2", text=self.m_Veiculo)
        self.listaPlaca.column("#2", width=120)
        self.listaPlaca.heading("#3", text=self.m_Montadora)
        self.listaPlaca.column("#3", width=170)
        self.listaPlaca.heading("#4", text=self.m_Cor)
        self.listaPlaca.column("#4", width=100)
        self.listaPlaca.heading("#5", text=self.m_Combustivel)
        self.listaPlaca.column("#5", width=100)
        self.listaPlaca.heading("#6", text=self.m_Ano)
        self.listaPlaca.column("#6", width=80)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janelaCli, orient='vertical',
                               command=self.listaPlaca.yview)
        # Adiciona barra de rolagem
        self.listaPlaca.configure(yscroll=self.barra.set)
        self.barra.place(relx=0.835, rely=0.7,
                         relwidth=0.02, relheight=0.27)

        self.listaPlaca.place(relx=0.02, rely=0.7,
                              relwidth=0.81, relheight=0.27)
        #    Binding da listbox
        self.listaPlaca.bind('<Double-1>', self.bind_autoC)
        ############################################################################
    def busca_autoC(self, *args):
        ### Widgets - Listar tecnicos ###
        self.nomeEquipEntry.insert(END, '%')

        veicAuto = self.nomeEquipEntry.get()

        self.listatec = Toplevel()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("420x240")
        self.listatec.resizable(FALSE, FALSE)
        self.listatec.transient(self.janelaCli)
        self.listatec.focus_force()
        self.listatec.grab_set()
        ##########
        self.listatec1 = ttk.Treeview(self.listatec, height=10, column=("col1", "col2", "col3"))
        self.listatec1.heading("#0", text="")
        self.listatec1.heading("#1", text='Cod')
        self.listatec1.heading("#2", text=self.m_Automovel)
        self.listatec1.heading("#3", text=self.m_Marca)

        self.listatec1.column("#0", width=0)
        self.listatec1.column("#1", width=40)
        self.listatec1.column("#2", width=180)
        self.listatec1.column("#3", width=150)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.listatec, orient='vertical', command=self.listatec1.yview)

        # Adiciona barra de rolagem
        self.listatec1.configure(yscroll=self.barra.set)
        self.barra.place(x=377, y=6, width=30, height=225)

        self.listatec1.place(x=5, y=5)
        self.conecta_Glac()

        self.cursor.execute("""SELECT cod_aut, automovel, marca FROM automoveis, montadora WHERE montadora.cod = automoveis.montad
             AND automovel LIKE '%s' ORDER BY automovel ASC""" % veicAuto)

        rows = self.cursor.fetchall()
        for row in rows:
            self.listatec1.insert("", END, values=row)

        # Binding da listbox
        self.listatec1.bind('<Double-1>', self.add_autobindC)

        self.desconecta_Glac()
    def deletar_windowC(self):
        self.listatec = Toplevel()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("380x85")
        self.listatec.resizable(FALSE, FALSE)
        self.listatec.transient(self.janelaCli)
        self.listatec.focus_force()
        self.listatec.grab_set()
        ##########
        def btnao():
            self.listatec.destroy()
        self.MensLabel = LabelGlac(self.listatec)
        self.MensLabel.configure(text=self.m_msgCertezaDel)
        self.MensLabel.place(x=10, y=10)

        self.BtSim = ButtonGlac(self.listatec)
        self.BtSim.configure(text=self.m_Sim,
                            command=self.del_clienteC)
        self.BtSim.place(relx=0.2, y=50, width=70)

        self.BtNao = ButtonGlac(self.listatec)
        self.BtNao.configure(text=self.m_Nao,
                             command=btnao)
        self.BtNao.place(relx=0.6, y=50, width=70)
    def deletar_windowPlacaC(self):
        self.listatec = Toplevel()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("380x85")
        self.listatec.resizable(FALSE, FALSE)
        self.listatec.transient(self.janelaCli)
        self.listatec.focus_force()
        self.listatec.grab_set()
        ##########
        def btnao():
            self.listatec.destroy()
        self.MensLabel = LabelGlac(self.listatec)
        self.MensLabel.configure(text=self.m_msgCertezaDel)
        self.MensLabel.place(x=10, y=10)

        self.BtSim = ButtonGlac(self.listatec)
        self.BtSim.configure(text=self.m_Sim,
                             command=self.del_placaC)
        self.BtSim.place(relx=0.2, y=50, width=70)

        self.BtNao = ButtonGlac(self.listatec)
        self.BtNao.configure(text=self.m_Nao,
                             command=btnao)
        self.BtNao.place(relx=0.6, y=50, width=70)