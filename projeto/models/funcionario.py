from numpy import double
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.fisica import Fisica
from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa
from projeto.models.enum.setor import Setor
from abc import ABC,abstractmethod

class Funcionario(ABC,Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, 
              dataNascimento: str,cpf:str,rg:str,matricula:str, setor:Setor,salario:double) -> None:
        super().__init__(nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.cpf= cpf
        self.rg= rg
        self.matricula = matricula
        self.setor= setor
        self.salario = salario
        super().__init__(nome, telefone, email, endereco,sexo)
    @abstractmethod
    def _verifica_salario(self,salario):
        if salario < 0:
            raise ValueError ("O salario deve ser maior que zero")
        if isinstance(salario,double):
            raise TypeError("Digite um numero valido")
        return salario
    
    def __str__(self) -> str:
        return super().__str__() + f"\nCPF:{self.cpf} \nRg:{self.rg}
        \n matricula{self.matricula} \nsetor{self.setor} \nSalario{self.salario}"