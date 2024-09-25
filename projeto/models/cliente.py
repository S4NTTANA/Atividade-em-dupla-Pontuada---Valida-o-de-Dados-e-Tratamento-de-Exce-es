from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.sexo import Sexo
from projeto.models.fisica import Fisica

class Cliente(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str,protocolo:int) -> None:
        self.protocolo = protocolo
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
    def __str__(self) -> str:
        return super().__str__() + f"\nProtocolo{self.protocolo}"
    