from reportlab.pdfgen import canvas
import platform
from funcs.backUteis import license
import webbrowser

plataforma = platform.system()

class PrintRel(license.Data_company):
    def VarRel(self):
        self.dados()
        ### VARIAVEIS DO RELATORIO
        self.dia_R = self.entradaDataorc.get()
        self.mes_R = self.entradaDataorc2.get()
        self.ano_R = self.entradaDataorc3.get()
        self.cliente_R = self.listNome.get()
        self.endereco_R = self.listEndereco.get()
        self.bairro_R = self.listBairro.get()
        self.municipio_R = self.listMunicipio.get()
        self.cpf_R = self.listCpf.get()
        self.fone_R = self.listFone.get()
        self.uf_R = self.listUf.get()
        self.obs_R = self.listObs.get()
        self.aut_R = self.listAut.get()
        self.anoAut_R = self.listAno.get()
        self.marca_R = self.listMarca.get()
        self.combustivel_R = self.listCombustivel.get()
        self.cor_R = self.listCor.get()
        self.placa_R = self.placa.get()
        self.numorc_R = self.listaNumOrc.get()
        self.area1_R = self.area1.get()
        self.area2_R = self.area2.get()
        self.area3_R = self.area3.get()
        self.area4_R = self.area4.get()
        self.km_R = self.entradaObs.get()
        self.comp1 = self.listInicio.get()
        self.comp2 = self.listFim.get()

        self.lista1_R = self.listaCol2a.get()
        self.colquant1_R = self.listaCol3a.get()
        self.colunit1_R = self.listaCol4a.get()
        self.coltotal1_R = self.listaCol5a.get()

        self.entradatotal2_R = self.entradatotal.get()
        self.tecnico_R = self.entradaTecnico.get()
        self.tiporc_R = self.Tipvar.get()
    def PrintOrc(self):
        if plataforma == "Linux":
            webbrowser.open("Orcamento.pdf")
            print(platform.system())
        else:
            url = "Orcamento.pdf"
            print(platform.system())
            webbrowser.open(url, new=2)
    def imprime_orc(self):
        self.VarRel()
        # Gerar Relatorio de orçamento
        if plataforma == "Linux":
            self.c = canvas.Canvas("Orcamento.pdf");
            self.c.setFont("Helvetica-Bold", 24)
        else:
            self.c = canvas.Canvas("Orcamento.pdf");
            self.c.setFont("Helvetica-Bold", 24)
        try:
            self.c.drawInlineImage("logoempresa.jpg", 150, 770, 300, 70)
        except:
            self.c.drawString(220, 790, self.m_SeuLogo)
        self.c.setFont("Helvetica-Bold", 14)

        #### MOLDURA E TITULOS DO RELATORIO
        if self.tiporc_R == 'Orçamento':
            self.c.drawString(250, 755, 'Orçamento' + " Nº  " + self.numorc_R)
        elif self.tiporc_R == "('Orçamento ',)":
            self.c.drawString(250, 755, 'Orçamento' + " Nº  " + self.numorc_R)
        elif self.tiporc_R == self.m_Orcamento:
            self.c.drawString(250, 755, 'Orçamento' + " Nº  " + self.numorc_R)
        elif self.tiporc_R == "('Ordem de Serviço ',)":
            self.c.drawString(250, 755, 'Ordem de Serviço' + " Nº  " + self.numorc_R)
        elif self.tiporc_R == "Ordem de Serviço ":
            self.c.drawString(250, 755, 'Ordem de Serviço' + " Nº  " + self.numorc_R)
        elif self.tiporc_R == self.m_Ordem:
            self.c.drawString(250, 755, 'Ordem de Serviço' + " Nº  " + self.numorc_R)
        else:
            self.c.drawString(250, 755, self.tiporc_R + " Nº  " + self.numorc_R)
        self.c.drawString(15, 770, 'Entrada: ' + self.comp1)
        self.c.drawString(15, 750, 'Saida  : ' + self.comp2)
        self.c.drawString(15, 720, self.m_DadosDoCliente)
        self.c.rect(10, 732, 200, 3, fill=True, stroke=False); self.c.rect(211, 722, 375, 3, fill=True, stroke=False)
        self.c.rect(10, 482, 3, 250, fill=True, stroke=False); self.c.drawString(205, 722, " \ ")
        self.c.drawString(15, 640, self.m_DadosDoVeiculo)
        self.c.rect(10, 652, 200, 3, fill=True, stroke=False); self.c.rect(211, 642, 375, 3, fill=True, stroke=False)
        self.c.rect(585, 482, 5, 240, fill=True, stroke=False); self.c.drawString(205, 642, " \ ")
        #
        self.c.rect(10, 592, 350, 3, fill=True, stroke=False);self.c.rect(361, 582, 225, 3, fill=True, stroke=False)
        self.c.drawString(355, 582, " \ ")
        #
        self.c.rect(10, 542, 350, 3, fill=True, stroke=False); self.c.rect(361, 532, 225, 3, fill=True, stroke=False)
        self.c.drawString(355, 532, " \ ")
        self.c.drawString(15, 480, self.m_ProdutosEServicos)
        self.c.rect(10, 492, 165, 3, fill=True, stroke=False);self.c.rect(175, 482, 415, 5, fill=True, stroke=False)
        self.c.drawString(440, 130, self.m_Total); self.c.drawString(515, 130, self.entradatotal2_R)
        self.c.setFont("Helvetica", 12)
        ##### FORMATAÇÃO DOS CAMPOS DO RELATORIO
        self.c.drawString(15, 700, self.m_Nome + ": ________________________________  ")
        self.c.drawString(285, 700, self.m_Fone + ": ______________  ")
        self.c.drawString(415, 700, self.m_Cpf + '/' + self.m_Cnpj + ": _______________  ")
        self.c.drawString(15, 680, self.m_Endereco + ": ________________________________________")
        self.c.drawString(350, 680, self.m_Bairro + ": _____________________________")
        self.c.drawString(15, 660, self.m_Cidade + ": ______________________________________")
        self.c.drawString(335, 660, self.m_Uf + ": ____")
        self.c.drawString(15, 620, self.m_Placa + ": __________")
        self.c.drawString(120, 620, self.m_Veiculo + ": ______________________________")
        self.c.drawString(420, 620, self.m_Cor + ": __________________")
        self.c.drawString(90, 600, self.m_Combustivel + ": _______________________________")
        self.c.drawString(420, 600, self.m_Km + ": __________")
        self.c.drawString(14, 472,
                          "______________________________________________________________________________________")
        self.c.drawString(15, 460, self.m_Item); self.c.drawString(150, 460, self.m_Descricao)
        self.c.drawString(480, 460, self.m_Quant);  self.c.drawString(420, 460, self.m_ValorUnit)
        self.c.drawString(540, 460, self.m_Total);
        self.c.drawString(12, 460,
                          "______________________________________________________________________________________")

        linhaItem = "______________________________________________________________________________________"

        self.c.drawString(13, 450, linhaItem);   self.c.drawString(13, 440, linhaItem)
        self.c.drawString(13, 430, linhaItem);   self.c.drawString(13, 420, linhaItem)
        self.c.drawString(13, 410, linhaItem);   self.c.drawString(13, 400, linhaItem)
        self.c.drawString(13, 390, linhaItem);   self.c.drawString(13, 380, linhaItem)
        self.c.drawString(13, 370, linhaItem);   self.c.drawString(13, 360, linhaItem)
        self.c.drawString(13, 350, linhaItem);   self.c.drawString(13, 340, linhaItem)
        self.c.drawString(13, 330, linhaItem);   self.c.drawString(13, 320, linhaItem)
        self.c.drawString(13, 310, linhaItem);   self.c.drawString(13, 300, linhaItem)
        self.c.drawString(13, 290, linhaItem);   self.c.drawString(13, 280, linhaItem)
        self.c.drawString(13, 270, linhaItem);   self.c.drawString(13, 260, linhaItem)
        self.c.drawString(13, 250, linhaItem);   self.c.drawString(13, 240, linhaItem)
        self.c.drawString(13, 230, linhaItem);   self.c.drawString(13, 220, linhaItem)
        self.c.drawString(13, 210, linhaItem);   self.c.drawString(13, 200, linhaItem)
        self.c.drawString(13, 190, linhaItem);   self.c.drawString(13, 180, linhaItem)
        self.c.drawString(13, 170, linhaItem);   self.c.drawString(13, 160, linhaItem)

        ## MOLDURAS DO RELATORIO
        self.c.rect(10, 155, 2, 330, fill=True, stroke=False), self.c.rect(40, 155, 2, 314, fill=True, stroke=False)
        self.c.rect(420, 155, 2, 314, fill=True, stroke=False), self.c.rect(475, 155, 2, 314, fill=True, stroke=False)
        self.c.rect(515, 155, 2, 314, fill=True, stroke=False), self.c.rect(585, 155, 4, 330, fill=True, stroke=False)
        self.c.rect(13, 155, 570, 2, fill=True, stroke=False)

        self.c.setFont("Helvetica", 10)

        ####  TEXTO DE DESCRICAO DOS PROBLEMAS
        self.c.drawString(50, 565, self.area1_R)
        self.c.drawString(50, 550, self.area2_R)
        self.c.drawString(50, 515, self.area3_R)
        self.c.drawString(50, 500, self.area4_R)

        self.c.setFont("Helvetica-Bold",10)
        self.c.drawString(15, 585, self.m_Atend1print)
        self.c.drawString(15, 535, self.m_Atend2print)

        #### DADOS DO CLIENTE
        self.c.rect(15, 745, 570, 2, fill=True, stroke=False)
        self.c.drawString(65, 700,  self.cliente_R)
        self.c.drawString(325, 700,  self.fone_R  )
        self.c.drawString(485, 700,  self.cpf_R  )
        self.c.drawString(80, 680,  self.endereco_R  )
        self.c.drawString(410, 680,  self.bairro_R  )
        self.c.drawString(85, 660,  self.municipio_R  )
        self.c.drawString(375, 660, self.uf_R)
        #### DADOS DO AUTOMOVEL
        self.c.drawString(60, 620,  self.placa_R  )
        self.c.drawString(165, 620,  self.aut_R  )
        self.c.drawString(320, 620, self.marca_R)
        self.c.drawString(470, 620, self.cor_R)
        self.c.drawString(180, 600, self.combustivel_R)
        self.c.drawString(450, 600, self.km_R)

        self.c.setFont("Helvetica", 8)

        #### DESCRIÇÃO DOS ITENS DO ORÇAMENTO

        ### Item 1
        self.conecta_Glac()

        id_orc = self.listaNumOrc.get()

        #########
        self.cursor.execute("""SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s'  """ % id_orc)
        rows = self.cursor.fetchall()
        x = 460
        for row in rows:
            row = str(row)
            row = row.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
            x -= 10
            self.c.drawString(45, x, row)

        self.c.setFont("Helvetica", 10)
        ########
        self.cursor.execute("""SELECT ordem_item FROM orcamento2 WHERE id_orc2 = '%s'  """ % id_orc)
        rows = self.cursor.fetchall()
        x = 460
        for row in rows:
            row = str(row)
            row = row.replace('(', '').replace(')', '').replace(',', '')
            x -= 10
            self.c.drawString(25, x, row)

        ########
        self.cursor.execute("""SELECT valor FROM orcamento2 WHERE id_orc2 = '%s'  """ % id_orc)
        rows = self.cursor.fetchall()
        x = 460
        for row in rows:
            row = str(row)
            row = row.replace('(', '').replace(')', '').replace("'", "").replace("$,", "$")
            x -= 10
            self.c.drawString(430, x, row)
        ########
        self.cursor.execute("""SELECT quant FROM orcamento2 WHERE id_orc2 = '%s'  """ % id_orc)
        rows = self.cursor.fetchall()
        x = 460
        for row in rows:
            row = str(row)
            row = row.replace('(', '').replace(',)', '').replace("'", "")
            x -= 10
            self.c.drawString(480, x, row)
        ########
        self.cursor.execute("""SELECT total FROM orcamento2 WHERE id_orc2 = '%s'  """ % id_orc)
        rows = self.cursor.fetchall()
        x = 460
        for row in rows:
            row = str(row)
            row = row.replace('(', '').replace(',)', '').replace("'", "")
            x -= 10
            self.c.drawString(520, x, row)
        ########

        self.desconecta_Glac()


        self.c.setFont("Helvetica", 12)
        #### VARIAVEIS DO RODAPE DO RELATORIO - DADOS DA EMPRESA
        self.c.rect(15, 100, 570, 5, fill=True, stroke=False)
        self.c.drawString(30, 80, self.NomeEmpresa);
        self.c.drawString(30, 60, self.NomeRuaEmp)
        self.c.drawString(300, 60, self.NomeBairroEmp);
        self.c.drawString(430, 60, self.MunicipioEmp)
        self.c.drawString(30, 40, self.TelefoneEmp);
        self.c.drawString(30, 20, self.m_Tecnico + self.tecnico_R);
        self.c.setFont("Helvetica", 8)
        self.c.drawString(280, 5, "GlacX - Oficinas - RfZorzi Sistemas - https://www.facebook.com/rfzorzi/")
        self.c.showPage()
        self.c.save()
        self.PrintOrc()
    def PrintVist(self):
        if plataforma == "Linux":
            webbrowser.open("Vistoria.pdf")
            print(platform.system())
        else:
            webbrowser.open("Vistoria.pdf", new=2)
    def imprime_vist(self):
        self.VarRel()
        self.tecnico_R = self.entradaTecnico.get();
        self.tiporc_R = self.Tipvar.get()

        if plataforma == "Linux":
            self.c = canvas.Canvas("Vistoria.pdf");
            self.c.setFont("Helvetica-Bold", 24)
        else:
            self.c = canvas.Canvas("Vistoria.pdf");
            self.c.setFont("Helvetica-Bold", 24)
                #### MOLDURA E TITULOS DO RELATORIO

        try:
            self.c.drawInlineImage("logoempresa.jpg", 150, 770, 300, 70)
        except:
            self.c.drawString(220, 790, 'Seu Logo')
        self.c.setFont("Helvetica-Bold", 16);
        self.c.drawString(200, 755, self.m_VistoriadoVeiculo + "Nº  " + self.numorc_R)
        self.c.setFont("Helvetica", 16)
        self.c.drawString(15, 750, self.m_Data + ': ' + self.dia_R + "/" + self.mes_R + "/" + self.ano_R)
        self.c.drawString(15, 720, self.m_DadosDoCliente)
        self.c.rect(10, 732, 200, 3, fill=True, stroke=False);
        self.c.rect(211, 722, 375, 3, fill=True, stroke=False)
        self.c.rect(10, 482, 3, 250, fill=True, stroke=False);
        self.c.drawString(205, 722, " \ ")
        self.c.drawString(15, 640, self.m_DadosDoVeiculo)
        self.c.rect(10, 652, 200, 3, fill=True, stroke=False);
        self.c.rect(211, 642, 375, 3, fill=True, stroke=False)
        self.c.rect(585, 482, 5, 240, fill=True, stroke=False);
        self.c.drawString(205, 642, " \ ")
        self.c.drawString(15, 580, self.m_ItensVistoriados)
        self.c.rect(10, 592, 195, 3, fill=True, stroke=False);
        self.c.rect(205, 582, 385, 5, fill=True, stroke=False)
        # Vistoria variaveis
        self.codVist_R = self.listaNumOrc.get();
        self.tanque_R = self.are1.get();
        self.odometro_R = self.are2.get()
        self.radio_R = self.are3.get();
        self.calota_R = self.are4.get();
        self.triangulo_R = self.are5.get()
        self.macaco_R = self.are6.get();
        self.estepe_R = self.are7.get();
        self.obs1_R = self.are8.get()
        self.obs2_R = self.are9.get()
        self.c.setFont("Helvetica-Bold", 14)
        ### Tanque
        self.c.drawString(35, 540, self.m_Tanque + self.m_ExtensLabel +
                          self.m_DoisPontos +  self.tanque_R)
        #### Odometro
        self.c.drawString(35, 500, self.m_Odometro + self.m_ExtensLabel +
                          self.m_DoisPontos +  self.odometro_R  )
        ### Obs 1
        self.c.drawString(35, 460, 'Obs 1' + self.m_ExtensLabel + self.m_DoisPontos +  self.radio_R  )
        ### Obs 2
        self.c.drawString(35, 420, 'Obs 2' + self.m_ExtensLabel + self.m_DoisPontos +  self.calota_R  )
        ### Obs 3
        self.c.drawString(35, 380, 'Obs 3' + self.m_ExtensLabel + self.m_DoisPontos +  self.triangulo_R  )
        ### Obs 4
        self.c.drawString(35, 340, 'Obs 4' + self.m_ExtensLabel + self.m_DoisPontos +  self.macaco_R  )
        ### Obs 5
        self.c.drawString(35, 300, 'Obs 5' + self.m_ExtensLabel + self.m_DoisPontos +  self.estepe_R  )
        ### Obs 6
        self.c.drawString(35, 260, 'Obs 6' + self.m_ExtensLabel + self.m_DoisPontos +  self.obs1_R  )
        ## Obs 7
        self.c.drawString(35, 220, 'Obs 7' + self.m_ExtensLabel + self.m_DoisPontos +  self.obs2_R  )
        self.c.setFont("Helvetica-Bold", 12);
        self.c.drawString(35, 180, self.m_ConfirmaVistoria)

        ##### FORMATAÇÃO DOS CAMPOS DO RELATORIO
        self.c.drawString(15, 700, self.m_Nome + ": ________________________________  ")
        self.c.drawString(285, 700, self.m_Fone + ": ______________  ")
        self.c.drawString(415, 700, self.m_Cpf + '/' +self.m_Cnpj + ": _______________  ")
        self.c.drawString(15, 680, self.m_Endereco + ": ________________________________________")
        self.c.drawString(350, 680, self.m_Bairro + ": _____________________________")
        self.c.drawString(15, 660, self.m_Cidade + ": ______________________________________")
        self.c.drawString(335, 660, self.m_Uf + ": ____")
        self.c.drawString(15, 620, self.m_Placa + ": __________")
        self.c.drawString(120, 620, self.m_Veiculo + ": ______________________________")
        self.c.drawString(420, 620, self.m_Cor + self.m_DoisPontos + "______________")
        self.c.drawString(90, 600, self.m_Combustivel + ": _______________________________")

        ## MOLDURAS DO RELATORIO
        self.c.rect(10, 155, 2, 330, fill=True, stroke=False);
        self.c.rect(13, 155, 570, 2, fill=True, stroke=False)
        self.c.rect(585, 155, 4, 330, fill=True, stroke=False);
        self.c.setFont("Helvetica", 10)

        #### DADOS DO CLIENTE
        self.c.rect(15, 745, 570, 2, fill=True, stroke=False)
        self.c.drawString(65, 700,  self.cliente_R);
        self.c.drawString(325, 700,  self.fone_R  )
        self.c.drawString(485, 700, self.cpf_R);
        self.c.drawString(80, 680,  self.endereco_R  )
        self.c.drawString(410, 680,  self.bairro_R);
        self.c.drawString(85, 660,  self.municipio_R)
        self.c.drawString(375, 660, self.uf_R);

        #### DADOS DO AUTOMOVEL
        self.c.drawString(60, 620, self.placa_R);
        self.c.drawString(180, 620,  self.aut_R  )
        self.c.drawString(440, 600,  self.marca_R);
        self.c.drawString(470, 620, self.cor_R)
        self.c.drawString(180, 600, self.combustivel_R);
        self.c.setFont("Helvetica-Bold", 12)

        #### VARIAVEIS DO RODAPE DO RELATORIO - DADOS DA EMPRESA
        self.c.rect(15, 100, 570, 5, fill=True, stroke=False)
        self.c.drawString(30, 80, self.NomeEmpresa);
        self.c.drawString(30, 60, self.NomeRuaEmp)
        self.c.drawString(300, 60, self.NomeBairroEmp);
        self.c.drawString(430, 60, self.MunicipioEmp)
        self.c.drawString(30, 40, self.TelefoneEmp)

        # self.c.drawString(30, 30, cab7)
        self.c.drawString(30, 20, self.m_Tecnico +  self.tecnico_R  );
        self.c.setFont("Helvetica", 8)
        self.c.drawString(280, 5, "GlacX - Oficinas - RfZorzi Sistemas - https://www.facebook.com/rfzorzi/")
        self.c.showPage()
        self.c.save()
        self.PrintVist()
