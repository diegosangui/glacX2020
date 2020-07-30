from funcs.modulos import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.gradienteFrame import *

class MaodeObra:
    def procedServ(self):
        ### Widgets - Listar Orçamentos ###
        self.listaOrc = Toplevel()
        self.listaOrc.title(" GLAC  ")
        self.listaOrc.configure(background='gray90', bd=6)
        self.listaOrc.geometry("300x100")
        self.listaOrc.resizable(FALSE, FALSE)
        self.listaOrc.transient(self.janela)
        self.listaOrc.focus_force()
        self.listaOrc.grab_set()

        self.MensLabel = Label(self.listaOrc, text=self.m_AtualizaMsg)
        self.MensLabel.place(x=10, y=10)

        self.listaNomeO = Entry(self.listaOrc, width=6, justify='right', bd=0,
            fg='#5c2f01', font=('Verdana', '12', 'bold'))
        self.listaNomeO.place(x=10, y=60)

        self.botaoBuscaNome = ButtonGlac(self.listaOrc)
        self.botaoBuscaNome.configure(text=self.m_Atualizar,
                                      command=self.procedServF)
        self.botaoBuscaNome.place(x=100, y=60, width=85, height=25)
    def procedServF(self):
        valorServ = self.listaNomeO.get()
        Serv = 's'

        self.conecta_Glac()

        self.cursor.execute("""
                 		UPDATE servprod SET valor = ? WHERE sp = ?""", (valorServ, Serv))
        self.conn.commit()

        self.desconecta_Glac()
        msg = "Valor atualizado com sucesso.\n "
        msg += ""
        messagebox.showinfo("GLAC", msg)
        self.listaOrc.destroy()
