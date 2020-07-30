from funcs.modulos import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.labelStyle import LabelGlac
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *

class CadPagamento:
    def add_pag(self):
        ordem = self.listaNumOrc.get()
        tipopag = self.listtipopag.get()
        valortotal = self.entryValorTotal.get()
        valordeduzir = self.entryValor.get()
        dia = self.diavar.get()
        mes = self.mesvar.get()
        ano = self.anovar.get()
        pago = "Não"

        self.conecta_Glac()

        self.cursor.execute("""
       		INSERT INTO formapag ( ordem, tipopag, valorpagar, valordeduzir, dia, mes , ano, pago)
       		VALUES ( ?, ?, ?, ?, ?, ?, ? , ?)""",
                       (ordem, tipopag, valortotal, valordeduzir, dia, mes, ano, pago))
        self.conn.commit()

        self.listaPag.delete(*self.listaPag.get_children())

        lista = self.cursor.execute("""
               SELECT  ordem, tipopag, valorpagar, valordeduzir, dia, mes, ano, pago
                FROM formapag WHERE ordem = '%s'  ORDER BY id ASC;
               """ % ordem)
        for i in lista:
            self.listaPag.insert("", END, values=i)

        informe = self.cursor.execute("""
            SELECT SUM(valordeduzir) FROM formapag WHERE ordem = '%s'   
            ORDER BY id ASC;
            """ % ordem)
        for i in informe:
            self.entryValorInform.delete(0, END)
            self.entryValorInform.insert(END, i)

        self.entryValor.delete(0, END)

        self.desconecta_Glac()
        self.janelaPagOrc.destroy()
        msg = "Pagamento incluido com sucesso"
        msg += ""
        messagebox.showinfo("GLAC - Pagamentos", msg)
        self.pagaOrdem()
    def mud_pag(self):
        self.conecta_Glac()

        tipopag = self.entry2.get()
        valor = self.entry3.get()
        diaA = self.entry4.get()
        mesA = self.entry5.get()
        anoA = self.entry6.get()
        pago = self.entry7.get()
        idA = self.entry9.get()

        self.cursor.execute(""" 
            UPDATE formapag SET tipopag = ?, valordeduzir = ?, dia = ?,
            mes = ?, ano = ?, pago = ? WHERE id = ? """,
            (tipopag, valor, diaA, mesA, anoA, pago, idA))
        self.conn.commit()

        self.desconecta_Glac()
        self.janPag2.destroy()
        self.janelaPagOrc.destroy()
        self.pagaOrdem()
    def carregaConsulta(self):
        self.conecta_Glac()

        tipopag = self.listtipopag.get()
        valor = self.entryValorDevido.get()

        mes = self.mesvar.get()
        ano = self.anovar.get()
        pago = self.entry7.get()


        self.listaPag.delete(*self.listaPag.get_children())

        lista = self.cursor.execute("""
            SELECT  ordem, tipopag, '*', valordeduzir, dia, mes, ano, pago, '*'
            FROM formapag WHERE tipopag = ? AND  mes = ? AND ano = ?
            AND pago = ? ORDER BY id ASC; """, (tipopag, mes, ano, pago))

        for i in lista:
            self.listaPag.insert("", END, values=i)

        self.entryValorDevido.delete(0, END)

        lista2 = self.cursor.execute("""
            SELECT  SUM(valordeduzir)
            FROM formapag WHERE tipopag = ? AND  mes = ? AND ano = ?
            AND pago = ? ORDER BY id ASC; """, (tipopag, mes, ano, pago))
        for i in lista2:
            if i == '':
                self.entryValorDevido.insert(END, "0.00")
            else:
                self.entryValorDevido.insert(END, i)

        self.desconecta_Glac()
    def carregaConsulta2(self):
        mes = self.mesvar2.get()
        ano = self.anovar2.get()
        pago = self.entry72.get()

        self.conn = sqlite3.connect("glac.db")
        self.cursor = self.conn.cursor()

        self.listaPag.delete(*self.listaPag.get_children())

        lista = self.cursor.execute("""
            SELECT  ordem, tipopag, '*', valordeduzir, dia, mes, ano, pago
            FROM formapag WHERE  mes = ? AND ano = ?
            AND pago = ? ORDER BY id ASC; """, (mes, ano, pago))
        for i in lista:
            self.listaPag.insert("", END, values=i)

        self.entryValorDevido.delete(0, END)

        lista2 = self.cursor.execute("""
            SELECT  SUM(valordeduzir)
            FROM formapag WHERE mes = ? AND ano = ?
            AND pago = ? ORDER BY id ASC; """, ( mes, ano, pago))
        for i in lista2:
            self.entryValorDevido.insert(END, i)


        self.conn.close()
