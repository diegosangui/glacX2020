from funcs.modulos import *

class ConsFinan:
    def OnDoubleClickFinan(self, event):
        self.limpa_produto()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServ.item(n, 'values')
            self.entradaCodprod.insert(END, col1)

            self.carrega_produto()
    def carrega_receita(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        self.listaServ2.delete(*self.listaServ2.get_children())

        ano = self.entry5.get()
        mes = self.entry6.get()

        lista = self.cursor.execute("""select id_orc1, placa_orc, dia, mes, ano, "R$",
            trim(replace(totalizador, ',', '.'),'R$') from orcamento1 where ano = '%s'
            and mes = '%s' and tipoOrc != 'Orçamento' order by dia asc;	""" % (ano, mes))

        for i in lista:
            print(i)
            self.listaServ.insert("", END, values=i)

        lista2 = self.cursor.execute("""
            select ano, mes, sum(trim(replace(totalizador, ',', '.'),'R$'))
            from orcamento1
            where ano = '%s' and mes = '%s'  and tipoOrc != 'Orçamento';
            """ % (ano, mes))
        for i in lista2:
            print(i)
            self.listaServ2.insert("", END, values=i)
        def carrega_produto_a(event):
            carrega_produto()

        self.desconecta_Glac()
    def limpa_receita(self):
        self.entradaReceita.delete(0, END)
        self.entradaCodReceita.delete(0, END)

        def limpa_produto_a(event):
            limpa_produto()
