from funcs.backUteis import imagensBase64, multilang, validadores, uteis
from funcs.backUteis import colors, conector, license, editItem
from funcs.backUteis import backAba2Front, backSegundoFrame
from Janelas import frontend
from Janelas.frontCads import cadAuto, cadClientes, cadEmpresa, cadMarcaProd
from Janelas.frontCads import cadEstoque, cadFornec, cadServ, cadProd
from Janelas.frontCads import cadPagamento, cadTec, AtMObra, consFinan


class Application(uteis.Functions, imagensBase64.ImagensBase64, conector.Conector,
        frontend.Tela, cadAuto.Automoveis, cadClientes.Clientes, multilang.Lang,
        colors.Colors, cadFornec.Fornecedores, cadTec.Tecnicos,
        validadores.Validadores, cadProd.Produtos, cadServ.Servicos,
        license.Data_company, cadMarcaProd.MarcaProdutos, AtMObra.MaodeObra,
        cadEmpresa.Empresa, cadEstoque.Estoque, consFinan.Financeiro,
        cadPagamento.PagamentoOrc, editItem.EditItens, backAba2Front.Aba2,
        backSegundoFrame.SegundoFrame):
    def __init__(self):
        self.cores()
        self.dados()
        self.multiGlacx()
        self.images_base64()
        self.tela()
        self.janela.mainloop()

Application()
