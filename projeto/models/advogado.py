from numpy import double
from projeto.models.enum.estadoCivil import EstadoCivil 
from projeto.models.endereco import Endereco
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.setor import Setor
from projeto.models.funcionario import Funcionario

class Advogado (Funcionario):
   def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: double, oab:str) -> None:
      self.oab = oab
      super().__init__(nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)

   
      

    