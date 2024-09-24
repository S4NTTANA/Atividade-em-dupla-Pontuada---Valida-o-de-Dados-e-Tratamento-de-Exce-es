
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.fisica import Fisica
from projeto.models.endereco import Endereco
from projeto.models.enum.setor import Setor
from abc import ABC,abstractmethod

class Funcionario(Fisica,ABC):
   
   def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str,cpf:str,rg:str,matricula:str,setor:Setor,salario:float) -> None:
       super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
       self.cpf= cpf
       self.rg= rg
       self.matricula = matricula
       self.setor= setor
       self.salario = self._verifica_salario(salario)
       super().__init__(nome, telefone, email, endereco,sexo)
   
   def _verifica_salario(self,salario:float)->float:
        if salario < 0:
            raise ValueError ("O salario deve ser maior que zero")
        if not isinstance(salario,float):
            raise TypeError("Digite um numero valido")
        return salario
    
   def __str__(self) -> str:
        return (super().__str__() + f"\nCPF:{self.cpf}" f"\nRg:{self.rg}"
        f"\n matricula{self.matricula}" f"\nsetor{self.setor}" f"\nSalario{self.salario}")