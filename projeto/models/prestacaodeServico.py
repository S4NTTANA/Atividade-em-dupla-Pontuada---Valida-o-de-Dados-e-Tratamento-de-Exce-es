from projeto.models.Juridica import Juridica
from projeto.models.endereco import Endereco

class Prestacaodeservicos(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str,contratoInicio :str ,contratoFim:str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.contratoInicio= contratoInicio
        self.contratoFim = contratoFim
        
        #super().__init__(id,nome, telefone, email, endereco, cnpj, inscricaoEstadual,contratoInicio,contratoFim)
    def __str__(self) -> str:
        return super().__str__() + f"\ncontratoInicio:{self.contratoInicio} \ncontratoFim{self.contratoFim}"
    def _Verifica__Id(self, id):
     return super()._Verifica__Id(id)
