from funcs.modulos import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.autcomplety import *

class QuintoFrame:
    def quinto_frame(self):
        #### Caixa de Seleção de Orçamento ou Ordem de Serviço
        self.Tipvar = StringVar()
        self.TipV = (self.m_Ordem, self.m_Orcamento);
        self.Tipvar.set(self.m_Orcamento)
        self.popupMenu = OptionMenu(self.top5, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx= 0.05,rely= 0.2,width= 160,height=35)

        ###  Label Licença
        self.licenciamento = Label(self.top5, text= self.Licenca, bd=0,
            bg=self.fundo_do_frame, fg=self.bg_button,font=('Verdana', '12', 'bold'));
        self.licenciamento.place(relx=0.3, rely=0.05, relwidth=0.3, relheight=0.4)

        ## Botao Acesse nossa pagina
        self.licenciamentoBt = ButtonGlac(self.top5)
        self.licenciamentoBt.configure(text=self.m_Acesse, command=self.PaginaRf)
        self.licenciamentoBt.place(relx=0.3, rely=0.6, relwidth=0.3, relheight=0.4)

        ###  Botao Imprimir Orçamento
        self.botaoImprimirOrc = Button(self.top5, image=self.button_imprime2,
            command=self.imprime_orc)
        self.botaoImprimirOrc.place(relx=0.74, rely=0.05, width=69, height=47)

        def funcpag():
            if self.listaNumOrc.get() == "":
                msg = "É necessário que um Orçamento ou Ordem de Serviço esteja " \
                      "devidamente carregada na tela!!!"
                messagebox.showinfo("GLAC", msg)
            elif self.listaNumOrc.get() == "Numero":
                msg = "É necessário que um Orçamento ou Ordem de Serviço esteja " \
                      "devidamente carregada na tela!!!"
                messagebox.showinfo("GLAC", msg)
            else:
                self.pagaOrdem()

        ##############################################################################################################
        ## Botao Forma de Pagamento
        self.formapag = ButtonGlac(self.top5)
        self.formapag.configure( text=self.m_Forma, command=funcpag,
                                 font=('Aharoni','8','bold'))
        self.formapag.place(relx=0.84, rely=0.1, width= 150, height=40)

