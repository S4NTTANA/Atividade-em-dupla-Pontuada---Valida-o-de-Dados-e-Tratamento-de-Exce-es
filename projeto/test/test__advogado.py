import pytest
from projeto.models.enum.unidade_federativa import UnidadeFederativa
from projeto.models.enum.setor import Setor
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.sexo import Sexo
from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco

@pytest.fixture
def test_advogado():
        advogado_1 = Advogado (1,"Pedro ","55565","pedro@",Endereco("Rua a","57","terrio","404560","salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.
                               DIVORCIADO,"04/06/2004","117.556","555256","0022",Setor.JURIDICO, 1.500,"5555")
        return advogado_1
def tes_verifica_Id_advogado(test_advogado):
        with pytest.raises(TypeError, match= "Digite um numero inteiro"):
                Advogado(1,"Pedro ","55565","pedro@",Endereco("Rua a","57","terrio","404560","salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"04/06/2004","117.556","555256","0022",Setor.JURIDICO, 1.500,"5555")

                




