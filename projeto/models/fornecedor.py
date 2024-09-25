from projeto.models.Juridica import Juridica
from projeto.models.endereco import Endereco
class Fornecedor(Juridica):
    
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str,produto:str) -> None:
        self.produto = produto
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        
    def _Verifica__Id(self, id)->int:
     return super()._Verifica__Id(id)

    def __str__(self) -> str:
        return super().__str__() + f"\nProduto{self.produto}"
    