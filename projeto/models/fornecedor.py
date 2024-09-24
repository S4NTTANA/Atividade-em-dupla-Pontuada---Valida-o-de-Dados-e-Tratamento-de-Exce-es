from projeto.models.Juridica import Juridica
from projeto.models.endereco import Endereco
class fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
    def __str__(self) -> str:
        return super().__str__() + f"\nProduto{self.produto}"
    def _Verifica__Id(self, id):
     return super()._Verifica__Id(id)
