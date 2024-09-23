from numpy import double
import pytest
from projeto.models.enum.unidade_federativa import UnidadeFederativa
from projeto.models.enum.setor import Setor
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.sexo import Sexo
from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.funcionario import Funcionario


#class Advogado (Funcionario):
 #   def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str,
  #                rg: str, matricula: str, setor: Setor, salario: double, oab:str) -> None:
   #     super().__init__(nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)
    #    self.oab= oab

@pytest.fixture
def oab_valido():
        advogado1 = Advogado ("Pedro ","55565","pedro@",Endereco("Rua a","57","terrio","404560","salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"04/06/2004","117.556","555256","0022",Setor.JURIDICO, 1.500,"5555")
        return advogado1

def Verifica_oab_valido(oab_valido):
        assert oab_valido.oab == "5555"
    
def verefica_tipo_errado_oab(oab_valido):
        with pytest.raises(TypeError,match= "digite algo valido."):
            Advogado ("Pedro ","55565","pedro@",Endereco("Rua a","57","terrio","404560","salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"04/06/2004","117.556","555256","0022",Setor.JURIDICO, 1.500,"5555")
        
