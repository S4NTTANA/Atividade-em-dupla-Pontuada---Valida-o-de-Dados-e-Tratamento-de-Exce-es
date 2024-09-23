from projeto.models.Juridica import Juridica
from projeto.models.endereco import Endereco

class prestacaodeservicos(Juridica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str,contratoInicio:str,contratoFim:str) -> None:
        self.contratoInicio= contratoInicio
        self.contratoFim = contratoFim
        super().__init__(nome, telefone, email, endereco, cnpj, inscricaoEstadual,contratoInicio,contratoFim)
    def __str__(self) -> str:
        return super().__str__() + f"\ncontratoInicio:{self.contratoInicio} \ncontratoFim{self.contratoFim}"
