from tkinter import *
import sqlite3

class AutocompleteEntrySP(Entry):
    def __init__(self, *args, **kwargs):
        #### Creating query for autocomplete
        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()

        self.lista2 = cursor
        self.lista2.execute("""SELECT cod_sp, '*****', LOWER(servprod), ' - ', tiposerv,
            ' - ' , LOWER(id_marcaprod) FROM servprod """)
        self.lista3 = cursor.fetchall()
        self.zlist = []
        for tup in self.lista3:
            t = str(tup).replace("('", "").replace("',)", "").replace(")", "")\
                .replace("'", "").replace(",","").replace("(","")
            self.zlist.append(t)
        cursor.close()

        Entry.__init__(self, *args, **kwargs)
        self.lista = self.zlist
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()
        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection); self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)

        self.lb_up = False
    def changed(self, name, index, mode):
        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:
                if not self.lb_up:
                    self.lb = Listbox(width = 70, height = 11)
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.lb_up = True
                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END, w)

            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
    def selection(self, event):
        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)
    def up(self, event):
        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':
                self.lb.selection_clear(first=index)
                index = str(int(index) - 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)
    def down(self, event):
        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:
                self.lb.selection_clear(first=index)
                index = str(int(index) + 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)
    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]