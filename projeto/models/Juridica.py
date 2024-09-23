
from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa
class Juridica(Pessoa):
  def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco,cnpj:str,inscricaoEstadual:str) -> None:
    self.cnpj= cnpj
    self.inscricaoEstadual= inscricaoEstadual
    super().__init__(nome, telefone, email, endereco,cnpj,inscricaoEstadual)
    
  def __str__(self) -> str:
    return super().__str__() + f"\ncnpj{self.cnpj} \ninscriçãoEstadual{self.inscricaoEstadual}"
  