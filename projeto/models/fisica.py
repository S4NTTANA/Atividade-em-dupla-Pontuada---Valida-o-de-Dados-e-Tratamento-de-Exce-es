from projeto.models.endereco import Endereco
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.pessoa import Pessoa
from abc import ABC,abstractmethod

class Fisica(ABC,Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str) -> None:
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento
        super().__init__(nome, telefone, email, endereco)
        
    @abstractmethod
    def _verifica_dataNascimento(self,dataNascimento):
        if dataNascimento < 0 :
            raise ValueError ("Digite uma data de nascimento valido")
        return dataNascimento
            

    def __str__(self) -> str:
        return super().__str__() + f"\nSexo:{self.sexo}\nEstado Civil: {self.estadoCivil}\nData de NAscimento: {self.dataNascimento}"
    



