from projeto.models.Juridica import Juridica
from projeto.models.endereco import Endereco
class fornecedor(Juridica):
    
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str,produto:str) -> None:
        self.produto= produto
        super().__init__(nome, telefone, email, endereco, cnpj, inscricaoEstadual,produto)
    def __str__(self) -> str:
        return super().__str__() + f"\nProduto{self.produto}"
