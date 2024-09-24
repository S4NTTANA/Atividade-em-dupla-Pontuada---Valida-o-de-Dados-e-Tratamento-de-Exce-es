from projeto.models.endereco import Endereco
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.pessoa import Pessoa
from abc import ABC,abstractmethod

class Fisica(Pessoa,ABC):
   def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo:Sexo, estadoCivil:EstadoCivil,dataNascimento:str) -> None:
      self.sexo = Sexo
      self.estadoCivil = EstadoCivil
      self.dataNascimento= dataNascimento
      super().__init__(id, nome, telefone, email, endereco)
        
   def __str__(self) -> str:
        return super().__str__() + f"\nSexo:{self.sexo}\nEstado Civil: {self.estadoCivil}\nData de NAscimento: {self.dataNascimento}"
    



