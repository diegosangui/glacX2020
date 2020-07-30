from funcs.backUteis import imagensBase64, multilang, validadores, uteis
from funcs.backUteis import colors, conector, license, editItem
from funcs.backUteis import backAba2Front, backSegundoFrame
from Janelas import frontend
from Janelas.frontCads import cadAuto, cadClientes, cadEmpresa
from Janelas.frontCads import cadEstoque, cadFornec, cadMarcaProd
from Janelas.frontCads import cadPagamento, cadProd, cadServ
from Janelas.frontCads import cadTec, atualizaMaodeObra, consFinan

class Application(uteis.Functions, imagensBase64.ImagensBase64,
                  conector.Conector, frontend.Tela, cadAuto.Automoveis,
                  cadClientes.Clientes, multilang.Lang, colors.Colors,
                  cadFornec.Fornecedores, cadTec.Tecnicos,
                  validadores.Validadores, cadProd.Produtos,
                  cadServ.Servicos, license.Data_company,
                  cadMarcaProd.MarcaProdutos, atualizaMaodeObra.MaodeObra,
                  cadEmpresa.Empresa, cadEstoque.Estoque,
                  consFinan.Financeiro, cadPagamento.PagamentoOrc,
                  editItem.EditItens, backAba2Front.Aba2,
                  backSegundoFrame.SegundoFrame):
    def __init__(self):
        self.montaTabelas(); self.cores()
        self.dados(); self.multiGlacx()
        self.images_base64(); self.tela()
        self.janela.mainloop()

Application()
