from Janelas.frontTela.frontend_aba1 import *
from Janelas.frontTela.frontend_aba2 import *
from Janelas.frontTela.frontend_aba4 import *
from Janelas.frontTela.frontend_Menus import *
from Janelas.frontTela.frontend_buscaOrc import *
from Janelas.frontTela.frontend_busca_tecnico import *
from Janelas.frontTela.frontend_busca_servico import *
from Janelas.frontTela.frontend_busca_cliente import *
from Janelas.frontTela.frontend_Calendario import *
from Janelas.frontTela.frontend_QuintoFrame import *
from Janelas.frontTela.frontend_QuartoFrame import *
from Janelas.frontTela.frontend_TerceiroFrame import *
from Janelas.frontTela.frontend_SegundoFrame import *
from Janelas.frontTela.frontend_PrimeiroFrame import *
from Janelas.frontTela.frontend_Logo import *
from Janelas.frontTela.frontend_Molduras import *
from Janelas.frontTela.frontend_Containers import *

from funcs.backUteis.ValidaEntradas import *
from funcs.backUteis.imagensBase64 import *
from funcs.backUteis import relatorios
from funcs.modulos import *
from funcs.backUteis.multilang import *

plataforma = platform.system()
if plataforma == "Linux" :
    janela = tix.Tk()
else:
    janela = Tk()


class Tela(relatorios.PrintRel, BuscaOrc, BuscaTecnico,
           Busca_Serv, BuscaCliente, Calendario):
    ## Tela Principal do Aplicativo
    def tela(self):
        # Window assembly
        self.janela = janela
        self.janela.title(self.m_Orcamento + self.m_e + self.m_OrdemdeServico)
        self.janela.configure(background=self.fg_label)
        self.janela.geometry("1000x600")
        self.janela.resizable(TRUE, TRUE)
        self.janela.minsize(width=800, height=500)

        self.background_image = PhotoImage(file='landscape.png')
        self.background_label = Label(self.janela,
            image=self.background_image)
        self.background_label.place(relwidth=1,
            relheight=1)

        # Chama funções da classe
        ImagensBase64.var_imag_64(self)
        ValidaEntradas.validaEntradas(self)
        Containers.containers(self)
        Molduras.molduras(self)
        Logotipo.logotipo(self)
        PrimeiroFrame.primeiro_frame(self)
        SegundoFrame.segundo_frame(self)
        TerceiroFrame.terceiro_frame(self)
        QuartoFrame.quarto_frame(self)
        QuintoFrame.quinto_frame(self)

        MenusClass.Menus(self)
        Aba1.aba1(self)
        Aba2.aba2(self)
        Aba4.aba4(self)
    ## Tela de Edição do Item
    def altera_itens_orc(self, *args):
        self.altOrcW = Toplevel()
        self.altOrcW.title(self.m_EditItem)
        self.altOrcW.configure(background=self.fundo_do_frame)
        self.altOrcW.geometry("900x100")
        self.altOrcW.resizable(False, False)

        self.ordemItemL = LabelGlac(self.altOrcW)
        self.ordemItemL.configure(text = self.m_Ordem)
        self.ordemItemL.place(x=5, y=1, width= 60, height=24)

        self.ordemItem = Entry(self.altOrcW)
        self.ordemItem.place(x=5, y=25, width= 60, height=24)

        self.descrItemL = LabelGlac(self.altOrcW)
        self.descrItemL.configure(text = self.m_Descricao)
        self.descrItemL.place(x=70, y=1, height=24)

        self.descrItem = Entry(self.altOrcW, width = 80)
        self.descrItem.place(x=70, y=25, height=24)

        self.codigoItemL = LabelGlac(self.altOrcW)
        self.codigoItemL.configure(text = self.m_Codigo)
        self.codigoItemL.place(x=550, y=1, height=24)

        self.codigoItem = Entry(self.altOrcW, width = 10)
        self.codigoItem.place(x=550, y=25, height=24)

        self.valorItemL = LabelGlac(self.altOrcW)
        self.valorItemL.configure(text = self.m_Valor_R)
        self.valorItemL.place(x=635, y=1, height=24)

        self.valorItem = Entry(self.altOrcW, width = 10)
        self.valorItem.place(x=635, y=25, height=24)

        self.quantItemL = ButtonGlac(self.altOrcW )
        self.quantItemL.configure(text = self.m_Quant,
                                  command = self.altera_itens_orc_quant)
        self.quantItemL.place(x=720, y=1, height=24)

        self.quantItem = Entry(self.altOrcW, width = 10)
        self.quantItem.place(x=720, y=25)

        self.totalItemL = LabelGlac(self.altOrcW)
        self.totalItemL.configure(text = self.m_Reais + " " + self.m_Total)
        self.totalItemL.place(x=805, y=1, height=24)

        self.totalItem = Entry(self.altOrcW, width = 10)
        self.totalItem.place(x=805, y=25)

        self.altera_itenBt = ButtonGlac(self.altOrcW)
        self.altera_itenBt.configure(text = self.m_AlterarRegistro,
                                    command = self.altera_itens_orc_alterabt)
        self.altera_itenBt.place(x= 580, y=60, height= 25)

        self.deleta_itenBt = ButtonGlac(self.altOrcW)
        self.deleta_itenBt.configure(text = self.m_ExcluirRegistro,
                                    command = self.altera_itens_orc_deletabt)
        self.deleta_itenBt.place(x=740, y=60, height= 25)

        self.listaServProd.selection()
        for n in self.listaServProd.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServProd.item(n, 'values')
            self.ordemItem.insert(END, col1)
            self.descrItem.insert(END, col2)
            self.codigoItem.insert(END, col3)
            self.valorItem.insert(END, col4)
            self.quantItem.insert(END, col5)
            self.totalItem.insert(END, col6)
