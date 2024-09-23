from numpy import double
from projeto.models.endereco import Endereco
from projeto.models.enum.setor import Setor
from projeto.models.funcionario import Funcionario

class medico(Funcionario):
 def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, matricula: str, setor: Setor, salario: double,crm:str) -> None:
  self.crm = crm
  super().__init__(nome, telefone, email, endereco, cpf, rg, matricula, setor, salario)
  
  def __str__(self) -> str:
    return super().__str__() + f"\nCrm {self.crm}"


