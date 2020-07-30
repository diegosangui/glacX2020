from funcs.modulos import *
from Janelas.estiloWidgets.labelStyle import LabelGlac
from Janelas.estiloWidgets.autcomplety import *
from funcs.backCads.backCadEmpresa import *

class Empresa(CadEmpresa):
    def cademp(self):
        self.janelaEmp = Toplevel()
        self.janelaEmp.title('Glacx' + self.m_Empresa)
        self.janelaEmp.configure(background=self.fundo_da_tela)
        self.janelaEmp.geometry("410x250")
        self.janelaEmp.resizable(FALSE, FALSE)
        self.janelaEmp.transient(self.janela)
        self.janelaEmp.focus_force()
        self.janelaEmp.grab_set()

        self.descrNomeServ = LabelGlac(self.janelaEmp)
        self.descrNomeServ.configure(text=self.m_Estab)
        self.descrNomeServ.place(relx=0.2, rely=0.05, relwidth=0.6)

        self.cliente_canvas2 = Canvas(self.janelaEmp, width=380, height=190,
            cursor='X_cursor', bd=2, bg=self.fundo_do_frame)
        self.cliente_canvas2.place(x=8, y=38)

        self.entradaCod_emp = Entry(self.janelaEmp, width=6)

        ###  Descrição e Entrada Nome
        self.descrNome = LabelGlac(self.janelaEmp)
        self.descrNome.configure(text=self.m_Nome)
        self.descrNome.place(x=10, y=53, width=80)

        self.entradaNome_emp = Listbox(self.janelaEmp, height=1)
        self.entradaNome_emp.place(x=85, y=53, width=300)

        ###  Descrição e Entrada Enedereco
        self.descrEndereco = LabelGlac(self.janelaEmp)
        self.descrEndereco.configure(text=self.m_Endereco)
        self.descrEndereco.place(x=10, y=83, width=80)

        self.entradaEndereco_emp = Listbox(self.janelaEmp, height=1)
        self.entradaEndereco_emp.place(x=85, y=83, width=300)

        ###  Descrição e Entrada Bairro
        self.descrBairro = LabelGlac(self.janelaEmp)
        self.descrBairro.configure(text=self.m_Bairro )
        self.descrBairro.place(x=10, y=103, width=80)

        self.entradaBairro_emp = Listbox(self.janelaEmp, height=1)
        self.entradaBairro_emp.place(x=85, y=103, width=300)

        ###  Descrição e Entrada Municipio
        self.descrMunicipio = LabelGlac(self.janelaEmp)
        self.descrMunicipio.configure(text=self.m_Cidade)
        self.descrMunicipio.place(x=10, y=123, width=80)

        self.entradaMunicipio_emp = Listbox(self.janelaEmp, height=1)
        self.entradaMunicipio_emp.place(x=85, y=123, width=220)

        ###  Descrição e Entrada UF
        self.descrUf = LabelGlac(self.janelaEmp)
        self.descrUf.configure(text=self.m_Uf)
        self.descrUf.place(x=315, y=123, width=30)

        self.entradaUf_emp = Listbox(self.janelaEmp, height=1)
        self.entradaUf_emp.place(x=350, y=123, width=30)

        #  Descrição e Entrada Fone
        self.descrFone = LabelGlac(self.janelaEmp)
        self.descrFone.configure(text=self.m_Fone)
        self.descrFone.place(x=10, y=143, width=80)

        self.entradaFone_emp = Listbox(self.janelaEmp, height=1)
        self.entradaFone_emp.place(x=85, y=143, width=140)

        ###  Descrição e Entrada Cep
        self.descrCep = LabelGlac(self.janelaEmp)
        self.descrCep.configure(text=self.m_Cep)
        self.descrCep.place(x=230, y=143, width=40)

        self.entradaCep_emp = Listbox(self.janelaEmp, height=1)
        self.entradaCep_emp.place(x=270, y=143, width=115)

        ###  Descrição e Entrada Cpf
        self.descrCpf = LabelGlac(self.janelaEmp)
        self.descrCpf.configure(text=self.m_Cnpj)
        self.descrCpf.place(x=10, y=163, width=80)

        self.entradaCpf_emp = Listbox(self.janelaEmp, height=1)
        self.entradaCpf_emp.place(x=85, y=163, width=140)

        ###  Descrição e Entrada Rg
        self.descrRg = LabelGlac(self.janelaEmp)
        self.descrRg.configure(text=self.m_Cpf)
        self.descrRg.place(x=230, y=163, width=40)

        self.entradaRg_emp = Listbox(self.janelaEmp, height=1)
        self.entradaRg_emp.place(x=270, y=163, width=115)

        ###  Descrição e Entrada Obs
        self.descrObs = LabelGlac(self.janelaEmp)
        self.descrObs.configure(text=self.m_Obs)
        self.descrObs.place(x=10, y=193, width=80)

        self.entradaObs_emp = Listbox(self.janelaEmp, height=1)
        self.entradaObs_emp.place(x=85, y=193, width=300)

        self.conecta_Glac()

        lista = self.cursor.execute("""
                SELECT cod_emp FROM empresa;
                """)
        for i in lista:
            self.entradaCod_emp.insert(i, END)

        self.desconecta_Glac()

        self.carrega_empresa()
        self.janelaEmp.mainloop()

