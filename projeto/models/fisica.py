from projeto.models.endereco import Endereco
from projeto.models.enum.Sexo import Sexo
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str) -> None:
        self.sexo = Sexo
        self.estadoCivil = EstadoCivil
        self.dataNascimento = dataNascimento
        super().__init__(nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        

    def __str__(self) -> str:
        return super().__str__() + f"\nSexo: {self.sexo}\nEstado Civil: {self.estadoCivil}\nData de NAscimento: {self.dataNascimento}"
    



