from funcs.modulos import *
from funcs.backCads.backCadPagamento import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.labelStyle import *
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *
from Janelas.estiloWidgets.buttonStyle import *

class PagamentoOrc(CadPagamento):
    def consultapag(self):
        self.janelaPagOrc = Toplevel();
        self.janelaPagOrc.title("GlacX")
        self.janelaPagOrc.configure(background='lavender');
        self.janelaPagOrc.geometry("790x470")
        self.janelaPagOrc.resizable(FALSE, FALSE)
        self.janelaPagOrc.transient(self.janela)
        self.janelaPagOrc.focus_force()
        self.janelaPagOrc.grab_set()

        ### Label principal
        self.labelformapag = LabelGlac(self.janelaPagOrc)
        self.labelformapag.configure(
            text=self.m_Consulta + ' ' + self.m_Pagamento)
        self.labelformapag.place(relx=0, rely=0,
                                 relwidth=1, height=25)

        ###  Frame Moldura
        self.frame3 = GradientFrame(self.janelaPagOrc)
        self.frame3.place(relx=0, rely=0.055,
                          relwidth=1, relheight=1)
        self.consulta1()
        self.consulta2()

        ### Lista de pagamentos
        self.listaPag = ttk.Treeview(self.frame3, height=10,
            column=("col1", "col2", "col3", "col4",
                    "col5", "col6", "col7", "col8", "col9"))

        self.listaPag.heading("#0", text="")
        self.listaPag.column("#0", width=0)
        self.listaPag.heading("#1", text= 'O.S')
        self.listaPag.column("#1", width=60)
        self.listaPag.heading("#2", text=self.m_Tipo)
        self.listaPag.column("#2", width=220)
        self.listaPag.heading("#3", text="")
        self.listaPag.column("#3", width=1)
        self.listaPag.heading("#4", text=self.m_Valor)
        self.listaPag.column("#4", width=120)
        self.listaPag.heading("#5", text=self.m_Dia)
        self.listaPag.column("#5", width=60)
        self.listaPag.heading("#6", text=self.m_Mes)
        self.listaPag.column("#6", width=60)
        self.listaPag.heading("#7", text=self.m_Ano)
        self.listaPag.column("#7", width=60)
        self.listaPag.heading("#8", text=self.m_Pago)
        self.listaPag.column("#8", width=110)
        self.listaPag.heading("#9", text="")
        self.listaPag.column("#9", width=1)
        self.listaPag.place(relx=0.02, rely=0.3, relwidth=0.92)

        # Cria barra de rolagem
        self.barraMov = Scrollbar(self.frame3, orient='vertical',
                                  command=self.listaPag.yview)
        self.barraMov.place(relx=0.94, rely=0.3,
                            width=20, height=220)

        self.listaPag.bind("<Double-1>" , self.OnDoubleClickpag)
        self.listaPag.configure(yscroll=self.barraMov.set)

        #### Frame do Valor a ser inserido
        self.frameValor = GradientFrame(self.frame3)
        self.frameValor.place(x=590, y=380,
                              width=175, height=52)

        ### Label do saldo a ser pago
        self.labelValor = LabelGlac(self.frame3)
        self.labelValor.configure(text=self.m_Valor + ' ' + self.m_Total)
        self.labelValor.place(x=600, y=385, width=150)

        self.labelCifrao = LabelGlac(self.frame3)
        self.labelCifrao.configure(text=self.m_Reais)
        self.labelCifrao.place(x=600, y=405, width=75)

        #### Entry do saldo a ser pago
        self.entryValorDevido = Entry(self.frame3)
        self.entryValorDevido.configure(validate="key")
        self.entryValorDevido.place(x=675, y=405, width=75)

        self.janelaPagOrc.mainloop()
    def consulta1(self):
        #### Frame do Valor a ser inserido
        self.frameValor = GradientFrame(self.frame3, 'lightblue')
        self.frameValor.place(relx=0.05, rely=0.018,
                              relwidth=0.9, height=55)

        #### Listbox do tipo de pagamento
        self.listtipopag = StringVar()
        self.listtipopag.set(self.m_Dinheiro)

        self.listtipopagV = {self.m_Debito, self.m_Credito, self.m_Dinheiro,
            self.m_Boleto, self.m_ChequePre, self.m_ChequeVista, self.m_Crediario,
            self.m_Promissoria, self.m_Desconto, self.m_Avista}
        self.listtipopagV = sorted(self.listtipopagV)

        self.popupMenu = OptionMenu(
            self.frameValor, self.listtipopag, *self.listtipopagV)
        self.popupMenu.place(relx=0.01, rely=0.5, width=130, height=20)

        tipoPag = LabelGlac(self.frameValor)
        tipoPag.configure(text= self.m_Tipo + ' ' + self.m_Pagamento)
        tipoPag.place(relx=0.01, rely=0.05, width=130, height=20)

        #### Entry data
        meslabel = LabelGlac(self.frameValor)
        meslabel.configure(text='Mês')
        meslabel.place(relx=0.22, rely=0.05, width=50, height=20)
        self.mesvar = StringVar()
        self.mesesV = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                       '11', '12'}
        self.mesesV = sorted(self.mesesV)
        self.mesvar.set(self.hj.month)
        self.popupMenu = OptionMenu(self.frameValor, self.mesvar, *self.mesesV)
        self.popupMenu.place(relx=0.22, rely=0.5, width=50, height=20)

        anolabel = LabelGlac(self.frameValor)
        anolabel.configure(text='Ano')
        anolabel.place(relx=0.31, rely=0.05, width=70, height=20)
        self.anovar = StringVar()
        self.anosV = {'2019', '2020', '2021', '2022', '2023', '2024', '2025',
            '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033',
            '2034', '2035', '2036', '2037', '2038'}
        self.anosV = sorted(self.anosV)
        self.anovar.set(self.hj.year)
        self.popupMenu = OptionMenu(self.frameValor, self.anovar, *self.anosV)
        self.popupMenu.place(relx=0.31, rely=0.5, width=70, height=20)

        ### Pago?
        pagolabel = LabelGlac(self.frameValor)
        pagolabel.configure(text=self.m_Pago)
        pagolabel.place(relx=0.43, rely=0.05, width=80, height=20)
        self.entry7 = StringVar()
        self.entry7V = { self.m_Sim, self.m_Nao}
        self.entry7V = sorted(self.entry7V)
        self.entry7.set(self.m_Sim)

        self.popupMenu = OptionMenu(self.frameValor, self.entry7, *self.entry7V)
        self.popupMenu.place(relx=0.43, rely=0.5, width=80, height=20)

        #### Button Inserir Registro
        self.btinserir = ButtonGlac(self.frameValor)
        self.btinserir.configure(
            text= self.m_Consulta + ' ' + self.m_Competência + self.m_barra +
            self.m_Tipo + self.m_barra + self.m_Pago,
            command=self.carregaConsulta)
        self.btinserir.place(relx=0.57, rely=0.48, width=300, height=23)
    def consulta2(self):
        #### Frame do Valor a ser inserido
        self.frameValor2 = GradientFrame(self.frame3, 'gray75')
        self.frameValor2.place(relx=0.05, rely=0.134,
                              relwidth=0.9, height=55)

        #### Entry data
        self.mesvar2 = StringVar()
        self.mesesV2 = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                       '11', '12'}
        self.mesesV2 = sorted(self.mesesV2)
        self.mesvar2.set(self.hj.month)
        self.popupMenu2 = OptionMenu(self.frameValor2, self.mesvar2, *self.mesesV2)
        self.popupMenu2.place(relx=0.051, rely=0.5,
                             width=75, height=20)
        mesValor2Label = LabelGlac(self.frameValor2)
        mesValor2Label.configure(text='Mês')
        mesValor2Label.place(relx=0.051, rely=0.05,
                             width=75, height=20)

        self.anovar2 = StringVar(self.frame3)
        self.anosV2 = {'2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028',
                      '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038'}
        self.anosV2 = sorted(self.anosV2)
        self.anovar2.set(self.hj.year)
        self.popupMenu2 = OptionMenu(self.frameValor2, self.anovar2, *self.anosV2)
        self.popupMenu2.place(relx=0.2, rely=0.5,
                             width=75, height=20)
        anoValor2label= LabelGlac(self.frameValor2)
        anoValor2label.configure(text= self.m_Ano)
        anoValor2label.place(relx=0.2, rely=0.05,
                             width=75, height=20)

        # Pago?
        self.entry72 = StringVar()
        self.entry7V2 = {self.m_Sim, self.m_Nao}
        self.entry7V2 = sorted(self.entry7V2)
        self.entry72.set(self.m_Sim)

        self.popupMenu2 = OptionMenu(self.frameValor2, self.entry72, *self.entry7V2)
        self.popupMenu2.place(relx=0.35, rely=0.5,
                             width=75, height=20)

        pagoValor2 = LabelGlac(self.frameValor2)
        pagoValor2.configure(text= self.m_Pago)
        pagoValor2.place(relx=0.35, rely=0.05,
                             width=75, height=20)

        #### Button Inserir Registro
        self.btinserir = ButtonGlac(self.frameValor2)
        self.btinserir.configure(
            text= self.m_Consulta + ' ' + self.m_Competência + self.m_barra
            + self.m_Pago, command=self.carregaConsulta2)
        self.btinserir.place(relx=0.57, rely=0.4, width = 300, height=25)
    def pagaOrdem(self):
        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()
        numAt = self.listaNumOrc.get()

        self.janelaPagOrc = Toplevel()
        self.janelaPagOrc.title("GlacX - Formas de Pagamento")
        self.janelaPagOrc.configure(background= self.fundo_da_tela)
        self.janelaPagOrc.geometry("800x445")
        self.janelaPagOrc.resizable(FALSE, FALSE)

        ###  Frame Moldura
        self.frame3 = GradientFrame(self.janelaPagOrc)
        self.frame3.place(relx=0, rely=0,
                          relwidth=1, relheight=1)

        # Label do numero de atendimento
        self.labelNumAtend = LabelGlac(self.janelaPagOrc)
        self.labelNumAtend.configure(text= self.m_NumAtend)
        self.labelNumAtend.place(relx=0.01, rely=0.01, height=20)

        # Entry do numero de atendimento
        self.entryNumAtend = Listbox(self.janelaPagOrc, height = 1)
        self.entryNumAtend.configure(bd=1, fg='brown', bg = 'lightgray',
            font=('Verdana', '8', 'bold'))
        self.entryNumAtend.place(relx=0.2, rely=0.01, width=80, height=20)
        self.entryNumAtend.insert(END, numAt)

        # Label do valor total
        self.labelValorTotal = LabelGlac(self.frame3)
        self.labelValorTotal.configure(text= self.m_Valor + ' ' + self.m_Total)
        self.labelValorTotal.place(relx=0.01, rely=0.05,
                                   relwidth=0.19, height=20)
        # Entry do valor total
        valorT = self.entradatotal.get()
        self.entryValorTotal = Entry(self.frame3)
        self.entryValorTotal.place(relx=0.2, rely=0.05,
                                   width=80, height=20)
        totalsimples = self.entradatotal.get()
        totalsimples = totalsimples.replace("R$","").replace(",",".")
        self.entryValorTotal.insert(END, totalsimples)

        ### Label do valor a ser inserido
        self.labelValor = LabelGlac(self.frame3)
        self.labelValor.configure(text= self.m_Valor)
        self.labelValor.place(relx=0.45, rely=0.01,
                              width = 80, height=20)

        self.labelCifrao = LabelGlac(self.frame3)
        self.labelCifrao.configure(text= self.m_Reais)
        self.labelCifrao.place(relx=0.45, rely=0.05,
                               width=20, height=20)

        #### Entry do valor a ser inserido
        self.entryValor = Entry(self.frame3)
        self.entryValor.configure(validate="key")
        self.entryValor.place(relx=0.475, rely=0.05,
                              width=60, height=20)
        self.entryValor.insert(END, '0.00')

        #### Listbox do tipo de pagamento
        self.listtipopag = StringVar()
        self.listtipopagV = {
            self.m_Debito, self.m_Credito, self.m_Dinheiro, self.m_Boleto,
            self.m_ChequePre, self.m_ChequeVista, self.m_Crediario,
            self.m_Promissoria, self.m_Desconto, self.m_Avista}
        self.listtipopagV = sorted(self.listtipopagV)
        self.listtipopag.set(self.m_Dinheiro)
        self.popupMenu = OptionMenu(
            self.frame3, self.listtipopag, *self.listtipopagV)
        self.popupMenu.place(relx=0.588, rely=0.05,
                           width=100, height=20)
        tipopaglabel = LabelGlac(self.frame3)
        tipopaglabel.configure(text= self.m_Tipo + ' ' + self.m_Pagamento,
                               font=('Verdana', 8 , 'bold'))
        tipopaglabel.place(relx=0.588, rely=0.01,
                           width=100, height=20)

        #### Data frame
        self.framedata = LabelGlac(self.frame3)
        self.framedata.configure(text='Data')
        self.framedata.place(relx=0.72, rely=0.01,
                             width=95, height=23)

        #### Entry data
        self.diavar = StringVar()
        self.diasV = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
            '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'}
        self.diasV = sorted(self.diasV)
        self.diavar.set(self.hj.day)
        self.popupMenu = OptionMenu(self.frame3, self.diavar, *self.diasV)
        self.popupMenu.place(relx=0.72, rely=0.04,
                             width=50, height=23)

        self.mesvar = StringVar()
        self.mesesV = {'1', '2', '3', '4', '5', '6',
                       '7', '8', '9', '10', '11', '12'}
        self.mesesV = sorted(self.mesesV)
        self.mesvar.set(self.hj.month)
        self.popupMenu = OptionMenu(self.frame3, self.mesvar, *self.mesesV)
        self.popupMenu.place(relx=0.75, rely=0.04,
                             width=50, height=23)

        self.anovar = StringVar()
        self.anosV = {'2019', '2020', '2021', '2022', '2023', '2024',
            '2025', '2026', '2027', '2028', '2029', '2030', '2031',
            '2032', '2033', '2034', '2035', '2036', '2037', '2038'}
        self.anosV = sorted(self.anosV)
        self.anovar.set(self.hj.year)
        self.popupMenu = OptionMenu(self.frame3, self.anovar, *self.anosV)
        self.popupMenu.place(relx=0.79, rely=0.04,
                             width=70, height=23)

        #### Data label
        self.labeldata = LabelGlac(self.frame3)
        self.labeldata.configure(text= self.m_Data)
        self.labeldata.place(relx=0.72, rely=0.01,
                             width=100, height=18)

        #### Button Inserir Registro
        self.btinserir = ButtonGlac(self.frame3)
        self.btinserir.configure(text= self.m_Inserir,
                                command= self.add_pag)
        self.btinserir.place(relx=0.84, rely=0.035,
                             width=120, height=27)

        ### Widgets - Listar pagamentos ###
        ### Lista de pagamentos
        self.listaPag = ttk.Treeview(self.frame3, height=14,
            column=("col1", "col2", "col3", "col4", "col5", "col6",
                    "col7", "col8", "col9"))
        self.listaPag.heading("#0", text="")
        self.listaPag.column("#0", width=0)
        self.listaPag.heading("#1", text= 'O.S')
        self.listaPag.column("#1", width=50)
        self.listaPag.heading("#2", text= self.m_Tipo)
        self.listaPag.column("#2", width=130)
        self.listaPag.heading("#3", text= self.m_Valor + ' ' + self.m_Pagamento)
        self.listaPag.column("#3", width=160)
        self.listaPag.heading("#4", text= self.m_ValorDeduzir)
        self.listaPag.column("#4", width=140)
        self.listaPag.heading("#5", text= self.m_Dia)
        self.listaPag.column("#5", width=51)
        self.listaPag.heading("#6", text= self.m_Mes)
        self.listaPag.column("#6", width=51)
        self.listaPag.heading("#7", text= self.m_Mes)
        self.listaPag.column("#7", width=51)
        self.listaPag.heading("#8", text= self.m_Pago)
        self.listaPag.column("#8", width=100)
        self.listaPag.heading("#9", text="")
        self.listaPag.column("#9", width=1)
        self.listaPag.place(relx=0.03, rely=0.12)

        # Cria barra de rolagem
        self.barraMov = Scrollbar(self.frame3, orient='vertical',
                                  command=self.listaPag.yview)
        self.barraMov.place(relx=0.95, rely=0.12,
                            width=20, height=305)

        self.listaPag.bind("<Double-1>", self.OnDoubleClickpag)
        self.listaPag.configure(yscroll=self.barraMov.set)

        ### Label do saldo a ser pago
        self.labelValor = LabelGlac(self.frame3)
        self.labelValor.configure(text= self.m_ValorDevido)
        self.labelValor.place(x=600, y=375, height=25)

        self.labelCifrao = LabelGlac(self.frame3)
        self.labelCifrao.configure(text="R$")
        self.labelCifrao.place(x=600, y=395, width=30, height=25)

        #### Entry do saldo a ser pago
        self.entryValorDevido = Entry(self.frame3)
        self.entryValorDevido.configure(validate="key")
        self.entryValorDevido.place(x=625, y=395, width=70, height=25)

        ### Label do saldo ja pago
        self.labelValor = LabelGlac(self.frame3)
        self.labelValor.configure(text= self.m_ValorInformado)
        self.labelValor.place(x=460, y=375, height=25)

        self.labelCifrao = LabelGlac(self.frame3)
        self.labelCifrao.configure(text= self.m_Reais)
        self.labelCifrao.place(x=460, y=395, width=30, height=25)

        #### Entry do saldo ja pago
        self.entryValorInform = Entry(self.frame3)
        self.entryValorInform.configure(validate="key")
        self.entryValorInform.place(x=490, y=395,
                                    width=85, height=25)

        lista = cursor.execute("""
            SELECT  ordem, tipopag, valorpagar, valordeduzir, dia, mes, ano, pago, id
            FROM formapag WHERE ordem = '%s'   ORDER BY id ASC;
            """ % numAt)
        for i in lista:
            self.listaPag.insert("", END, values=i)

        informe = cursor.execute("""
            SELECT SUM(valordeduzir) FROM formapag WHERE ordem = '%s' 
            ORDER BY id ASC;
            """ % numAt)
        for i in informe:
            self.entryValorInform.insert(END, i)

        rest1 = self.entryValorTotal.get()
        rest1 = float(rest1)
        rest2 = self.entryValorInform.get()
        rest2 = float(rest2)
        restante = rest1 - rest2
        self.entryValorDevido.insert(END, restante)

        conn.close()
        self.janelaPagOrc.mainloop()
    def OnDoubleClickpag(self, event):
        self.listaPag.selection()

        self.janPag2 = Toplevel()
        self.janPag2.title("GlacX")
        self.janPag2.configure(background='lavender');
        self.janPag2.geometry("600x85")
        self.janPag2.resizable(FALSE, FALSE)

        ## Entry NUm Atend
        self.label1 = LabelGlac(self.janPag2)
        self.label1.configure(text = "Nº O.S")
        self.label1.place(x=5, y=28, width=50, height=25)

        self.entry1 = Listbox(self.janPag2, width=8, height = 1)
        self.entry1.place(x=5, y=50, width=50, height=25)

        #### Listbox do tipo de pagamento
        self.entry2 = StringVar()
        self.entry2V = {self.m_Debito, self.m_Credito, self.m_Dinheiro, self.m_Boleto, self.m_ChequePre,
                        self.m_ChequeVista, self.m_Crediario, self.m_Promissoria, self.m_Desconto, self.m_Avista}
        self.entry2V = sorted(self.entry2V)
        self.popupMenu = OptionMenu(self.janPag2, self.entry2, *self.entry2V)
        self.popupMenu.place(x=65, y=50, width=130, height=25)
        labelTipopag2 = LabelGlac(self.janPag2)
        labelTipopag2.configure(text= self.m_Tipo + ' ' + self.m_Pagamento)
        labelTipopag2.place(x=65, y=28, width=130, height=25)

        #### Valor da parcela
        self.label1 = LabelGlac(self.janPag2)
        self.label1.configure(text= self.m_Valor_R)
        self.label1.place(x=205, y=28, width=80, height=25)

        self.entry3 = EntPlaceHold(self.janPag2, '')
        self.entry3.place(x=205, y=50, width=80, height=25)

        ### dia
        self.label1 = LabelGlac(self.janPag2)
        self.label1.configure(text="Data/Pagam")
        self.label1.place(x=295, y=30, width=120)

        self.entry4 = EntPlaceHold(self.janPag2, '')
        self.entry4.place(x=295, y=50, width=30, height=25)

        self.entry5 = StringVar()
        self.entry5V = {'1','2','3','4','5','6','7','8','9','10','11','12'}
        self.entry5V = sorted(self.entry5V)
        self.entry5.set(self.hj.month)
        self.entryMes = OptionMenu(self.janPag2, self.entry5, *self.entry5V)
        self.entryMes.place(x=325, y=50, width=50, height=25)

        self.entry6 = StringVar()
        self.entry6V = {'2020', '2021', '2022', '2023', '2024', '2025'}
        self.entry6V = sorted(self.entry6V)
        self.entry6.set(self.hj.year)
        self.entryAno = OptionMenu(self.janPag2, self.entry6, *self.entry6V)
        self.entryAno.place(x=375, y=50, width=65, height=25)

        ### Pago?
        self.label1 = LabelGlac(self.janPag2)
        self.label1.configure(text=self.m_Pago)
        self.label1.place(x=425, y=30, width=65, height=25)

        self.entry7 = StringVar()
        self.entry7V = {self.m_Sim, self.m_Nao}
        self.entry7V = sorted(self.entry7V)
        self.entry7.set("Sim")
        self.popupMenu = OptionMenu(self.janPag2, self.entry7, *self.entry7V)
        self.popupMenu.place(x=425, y=50, width=65, height=25)

        ### Alterar registro
        self.button1 = ButtonGlac(self.janPag2)
        self.button1.configure(text=self.m_Alterar,
                              command=self.mud_pag)
        self.button1.place(x=500, y=47)

        self.entry9 = Entry(self.janPag2)

        for n in self.listaPag.selection():
            col1,col2,col3,col4,col5,\
                col6,col7,col8,col9=self.listaPag.item(n, 'values')
            self.entry1.insert(END, col1)
            self.entry2.set(col2)
            self.entry3.insert(END, col4)
            self.entry4.insert(END, col5)
            self.entry5.set(col6)
            self.entry6.set(col7)
            self.entry7.set(col8)
            self.entry9.insert(END, col9)

        self.janPag2.mainloop()