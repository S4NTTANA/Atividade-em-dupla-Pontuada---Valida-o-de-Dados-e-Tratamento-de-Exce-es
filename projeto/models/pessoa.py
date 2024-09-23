from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self, id:int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = self._Verifica__Id (id)
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod 
    def _Verifica__Id(self,id): 
        if id < 0: 
            raise ValueError("O id não pode ser negativo")
        if isinstance (id,int):
            raise TypeError("Digite um numero inteiro")
        return id 
        
    
    def __str__(self) -> str:
        return (
                f"\nId: {self.id}"
                f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereço: {self.endereco}"
            )