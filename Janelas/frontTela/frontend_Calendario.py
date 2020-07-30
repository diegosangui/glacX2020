from funcs.modulos import *
from Janelas.estiloWidgets.autcomplety import *

class Calendario:
    def calendarioInicio(self):
        self.calendario1 = Calendar(self.top3, fg='gray75', bg=self.fundo_da_tela,
            font=('Times', '9', 'bold'),  locale = 'pt_br')
        self.calendario1.place(relx=0.05, rely=0.14,
                               relheight=0.6, relwidth = 0.2)

        self.calDataInicio = Button(self.top3, text='Inserir data inicial', command=self.print_calInicio,
            fg='gray35', font=('Times', '10', 'bold'))
        self.calDataInicio.place(relx=0.05, rely=0.74,
                                 relheight=0.1, relwidth = 0.2)
    def print_calInicio(self):
        dataInicio = self.calendario1.get_date()
        self.calendario1.destroy()
        self.listInicio.delete(0, END)
        self.listInicio.insert(END, dataInicio)
        self.calDataInicio.destroy()
    def calendarioFim(self):
        self.calendario2 = Calendar(self.top3, text=self.m_Estab, fg='gray75',
            bg=self.fundo_da_tela, locale = 'pt_br', font=('Times', '9', 'bold'))
        self.calendario2.place(relx=0.05, rely=0.14, relheight=0.6, relwidth = 0.2)

        self.calDataFim = Button(self.top3, text='Inserir data final', command=self.print_calFim,
                                 fg='gray35', font=('Times', '10', 'bold'))
        self.calDataFim.place(relx=0.05, rely=0.74, relheight=0.1, relwidth = 0.2)
    def print_calFim(self):
        dataFim = self.calendario2.get_date()
        self.listFim.delete(0, END)
        self.listFim.insert(END, dataFim)
        self.calendario2.destroy()
        self.calDataFim.destroy()
