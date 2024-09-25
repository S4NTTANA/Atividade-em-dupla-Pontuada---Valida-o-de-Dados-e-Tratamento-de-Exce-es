from enum import Enum

class UnidadeFederativa(Enum):
    BAHIA = ("Bahia", "Ba")
    SAO_PAULO = ("São Paulo","Sp")
    RIO_DE_JANEIRO = ("Rio de Janeiro","RJ")
    
    def __init__(self,estado:str,sigla:str) -> None:
        self.estado = estado
        self.sigla = sigla
        