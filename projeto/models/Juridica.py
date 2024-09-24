from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa
class Juridica(Pessoa,ABC):
  def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco,cnpj:str,inscricaoEstadual:str) -> None:
    super().__init__(id, nome, telefone, email, endereco)
    self.cnpj= cnpj
    self.inscricaoEstadual= inscricaoEstadual
    super().__init__(nome, telefone, email, endereco)
    
  def __str__(self) -> str:
    return super().__str__() + f"\ncnpj{self.cnpj} \ninscriçãoEstadual{self.inscricaoEstadual}"
  

  def _Verifica__Id(self, id):
    return super()._Verifica__Id(id)