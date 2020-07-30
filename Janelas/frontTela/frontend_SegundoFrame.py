from funcs.modulos import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.autcomplety import *
from Janelas.estiloWidgets.labelStyle import *

class SegundoFrame:
    def segundo_frame(self):
        ####                Container de cadastro do cliente
        #Label cod
        codigoCliente = LabelGlac(self.FrameCliente)
        codigoCliente.configure(text='Cod',
                                font=('Verdana', 8, 'bold'))
        codigoCliente.place(relx=0, rely=0.04,
                                  relwidth = 0.13, relheight= 0.17)
        # Entrada do Codigo do Cliente
        self.entradaCod_cli= Entry(self.FrameCliente,
            validate="key",validatecommand=self.vcmd6)
        self.entradaCod_cli.place(relx=0.1, rely=0.04,
                                  relwidth = 0.13, relheight= 0.17)

        try:
            self.bal_entCod = tix.Balloon()
            self.bal_entCod.bind_widget(self.entradaCod_cli,
                balloonmsg = "Código do cliente")
        except:
            pass

        # Botão Carrega
        self.botaoAdd = ButtonGlac(self.FrameCliente)
        self.botaoAdd.configure(text = self.m_Buscar,
                                command= self.busca_cliente)
        self.botaoAdd.place(relx=0.34, rely=0.011,
                            relwidth = 0.17, relheight= 0.21)

        try:
            self.bal_btCarr = tix.Balloon()
            self.bal_btCarr.bind_widget(self.botaoAdd,
                balloonmsg = "Botao para buscar o cadastro do cliente")
        except:
            pass

        # Botão Limpa
        self.botaoLimp = ButtonGlac(self.FrameCliente)
        self.botaoLimp.configure(text = self.m_Limpar,
                                 command=self.limpa_cliente)
        self.botaoLimp.place(relx=0.52, rely=0.011,
                             relwidth = 0.17, relheight= 0.21)

        try:
            self.bal_btLimp = tix.Balloon()
            self.bal_btLimp.bind_widget(self.botaoLimp,
                balloonmsg="Botão para limpar a tela de cadastro")
        except:
            pass

        ### Variavel do dia de hoje
        self.hj = date.today()
        # Label data
        self.descrData = LabelGlac(self.FrameCliente)
        self.descrData.configure(text= self.m_Data)
        self.descrData.place(relx=0.7, rely=0.04,
                             relwidth = 0.1, relheight= 0.17)

        try:
            self.bal_lbData = tix.Balloon()
            self.bal_lbData.bind_widget(self.descrData,
                balloonmsg="Data atual")
        except:
            pass

        # Entrada Dia
        self.entradaDataorc = EntPlaceHold(self.FrameCliente, self.hj.day)
        self.entradaDataorc.configure(width=2, validate="key",
            validatecommand=self.vcmd2, fg='darkred', bg=self.bg_entry,
            font=('Verdana', '8', 'bold'))
        self.entradaDataorc.place(relx=0.8, rely=0.04, relwidth = 0.05,
            relheight= 0.17)
        # Entrada Mês
        self.entradaDataorc2 = Entry(self.FrameCliente, width=2,
            validate="key", font=('Verdana', '8', 'bold'))
        self.entradaDataorc2.configure(validatecommand=self.vcmd2,
            bg=self.bg_entry, justify='right', fg='darkred')
        self.entradaDataorc2.place(relx=0.85, rely=0.04,
                                   relwidth = 0.05, relheight= 0.17)
        self.entradaDataorc2.insert(END, self.hj.month)
        # Entrada Ano
        self.entradaDataorc3 = Entry(self.FrameCliente,
            font=('Verdana', '8', 'bold'), fg='darkred')
        self.entradaDataorc3.configure(width=4, validate="key",
            bg=self.bg_entry, validatecommand=self.vcmd4)
        self.entradaDataorc3.place(relx=0.9, rely=0.04,
                                   relwidth = 0.08, relheight= 0.17)
        self.entradaDataorc3.insert(END, self.hj.year)

        # Entrada do nome do cliente
        self.lbNome = LabelGlac(self.FrameCliente)
        self.lbNome.configure(text = 'Nome',
                              font=('Verdana', 8, 'bold'))
        self.lbNome.place(relx=0, rely=0.24,
                            relwidth = 0.15, relheight= 0.15)

        self.listNome = Entry(self.FrameCliente)
        self.listNome.place(relx=0.15, rely=0.24,
                            relwidth = 0.8, relheight= 0.15)

        try:
            self.bal_nome = tix.Balloon()
            self.bal_nome.bind_widget(self.listNome,
                balloonmsg="Nome do cliente")
        except:
            pass

        # Entrada do Endereço
        self.lbEndereco = LabelGlac(self.FrameCliente)
        self.lbEndereco.configure(text = 'Logradouro',
                                  font = ('Verdana', 8, 'bold'))
        self.lbEndereco.place(relx=0,rely=0.39,
                                relwidth=0.15,relheight= 0.15)

        self.listEndereco=Entry(self.FrameCliente)
        self.listEndereco.place(relx=0.15,rely=0.39,
                                relwidth=0.8,relheight= 0.15)

        # Entrada Bairro
        self.listBairro=Entry(self.FrameCliente)
        self.listBairro.place(relx=0.05, rely=0.54,
                              relwidth = 0.35, relheight= 0.15)

        # Entrada Municipio
        self.listMunicipio=Entry(self.FrameCliente)
        self.listMunicipio.place(relx=0.45,rely=0.54,
                                 relwidth=0.4,relheight= 0.15)

        # Entrada UF
        self.listUf=Entry(self.FrameCliente)
        self.listUf.place(relx=0.87, rely=0.54,
                          relwidth = 0.08, relheight= 0.15)

        # Entrada CPF CNPJ
        self.lbCpfCnpj = LabelGlac(self.FrameCliente)
        self.lbCpfCnpj.configure(text='Cpf/Cnpj',
                                  font=('Verdana', 8, 'bold'))
        self.lbCpfCnpj.place(relx=0, rely=0.69,
                              relwidth=0.15, relheight=0.15)

        self.listCpf=Entry(self.FrameCliente)
        self.listCpf.place(relx=0.15, rely=0.69,
                           relwidth = 0.35, relheight= 0.15)

        # Entrada Fone
        self.lbFone = LabelGlac(self.FrameCliente)
        self.lbFone.configure(text='Fone',
                                 font=('Verdana', 8, 'bold'))
        self.lbFone.place(relx=0.5, rely=0.69,
                             relwidth=0.1, relheight=0.15)

        self.listFone=Entry(self.FrameCliente)
        self.listFone.place(relx=0.6, rely=0.69,
                            relwidth = 0.35, relheight= 0.15)

        # Entrada OBS
        self.lbObs = LabelGlac(self.FrameCliente)
        self.lbObs.configure(text='Observação',
                              font=('Verdana', 8, 'bold'))
        self.lbObs.place(relx=0, rely=0.84,
                          relwidth=0.15, relheight=0.15)

        self.listObs= Entry(self.FrameCliente)
        self.listObs.place(relx=0.15, rely=0.84,
                           relwidth = 0.8, relheight= 0.15)

        ###  		AUTOMOVEIS    ###  Listbox da Placa do Automovel
        ####  Lista de placas
        self.entradaCod_aut = Listbox(self.FrameAut2, width=11, height=9, bd=3,
            bg=self.fundo_do_frame, fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.entradaCod_aut.pack()
        # Binding da listbox da Placa
        self.entradaCod_aut.bind('<Button-1>', self.carrega_automovel)

        #### Frame do automovel

        # Placa
        self.lbPlaca = LabelGlac(self.FrameAut)
        self.lbPlaca.configure(text='Placa',
                              font=('Verdana', 8, 'bold'))
        self.lbPlaca.place(relx=0, rely=0.01,
                          relwidth=0.15, relheight=0.17)

        self.placa = Entry(self.FrameAut)
        self.placa.place(relx=0.15, rely=0.01,
                         relwidth=0.35, relheight=0.17)

        ###  Label e Entrada Ano
        self.lbPlaca = LabelGlac(self.FrameAut)
        self.lbPlaca.configure(text='Ano',
                               font=('Verdana', 8, 'bold'))
        self.lbPlaca.place(relx=0.5, rely=0.01,
                           relwidth=0.15, relheight=0.17)

        self.listAno = Entry(self.FrameAut)
        self.listAno.config(validate="key", validatecommand=self.vcmd4)
        self.listAno.place(relx=0.65, rely=0.01,
                           relwidth=0.2, relheight=0.17)

        ###  Label e Entrada Veiculo
        self.lbVeiculo = LabelGlac(self.FrameAut)
        self.lbVeiculo.configure(text='Veiculo',
                               font=('Verdana', 8, 'bold'))
        self.lbVeiculo.place(relx=0, rely=0.2,
                           relwidth=0.15, relheight=0.17)

        self.listAut = Entry(self.FrameAut)
        self.listAut.place(relx=0.15, rely=0.2,
                           relwidth=0.7, relheight=0.17)

        ###  Label e Entrada Marca
        self.lbMarca = LabelGlac(self.FrameAut)
        self.lbMarca.configure(text='Marca',
                                 font=('Verdana', 8, 'bold'))
        self.lbMarca.place(relx=0, rely=0.4,
                             relwidth=0.15, relheight=0.17)

        self.listMarca = Entry(self.FrameAut)
        self.listMarca.place(relx=0.15, rely=0.4,
                             relwidth=0.7, relheight=0.17)

        ###  Label e Entrada Combustivel
        self.lbFuel = LabelGlac(self.FrameAut)
        self.lbFuel.configure(text='Combust',
                               font=('Verdana', 8, 'bold'))
        self.lbFuel.place(relx=0, rely=0.6,
                           relwidth=0.15, relheight=0.17)

        self.listCombustivel = Entry(self.FrameAut)
        self.listCombustivel.place(relx=0.15, rely=0.6,
                                   relwidth=0.7, relheight=0.17)

        ###  Label e Entrada km
        self.lbKm = LabelGlac(self.FrameAut)
        self.lbKm.configure(text='Km',
                              font=('Verdana', 8, 'bold'))
        self.lbKm.place(relx=0, rely=0.8,
                          relwidth=0.15, relheight=0.17)

        self.entradaObs = Entry(self.FrameAut)
        self.entradaObs.config(validate="key", validatecommand=self.vcmd9float)
        self.entradaObs.place(relx=0.15, rely=0.8,
                              relwidth=0.2, relheight=0.17)

        ###  Label e Entrada Cor
        self.lbCor = LabelGlac(self.FrameAut)
        self.lbCor.configure(text='Cor',
                            font=('Verdana', 8, 'bold'))
        self.lbCor.place(relx=0.35, rely=0.8,
                        relwidth=0.15, relheight=0.17)

        self.listCor = Entry(self.FrameAut)
        self.listCor.place(relx=0.5, rely=0.8,
                           relwidth=0.35, relheight=0.17)

