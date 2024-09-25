import pytest
from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.setor import Setor
from projeto.models.enum.unidade_federativa import UnidadeFederativa

@pytest.fixture
def advogado_exemplo():
    advogado_1 = Advogado(
        1, "Pedro", "55565", "pedro@", 
        Endereco("Rua a", "57", "térreo", "404560", "Salvador", UnidadeFederativa.BAHIA), 
        Sexo.MASCULINO, EstadoCivil.DIVORCIADO, 
        "04/06/2004", "117.556", "555256", "0022", 
        Setor.JURIDICO, 1500, "5555"
    )
    return advogado_1




def test_verifica_Id_advogado():
    with pytest.raises(TypeError, match="Digite um id valido"):
        Advogado(
            "um", "Pedro", "55565", "pedro@", 
            Endereco("Rua a", "57", "térreo", "404560", "Salvador", UnidadeFederativa.BAHIA), 
            Sexo.MASCULINO, EstadoCivil.DIVORCIADO, 
            "04/06/2004", "117.556", "555256", "0022", 
            Setor.JURIDICO, 1500, "5555"
        )
def test_verifica_salario_tipo_advogado():
      with pytest.raises(TypeError, match= "Digite um salario valido"):
            Advogado(
            1, "Pedro", "55565", "pedro@", 
            Endereco("Rua a", "57", "térreo", "404560", "Salvador", UnidadeFederativa.BAHIA), 
            Sexo.MASCULINO, EstadoCivil.DIVORCIADO, 
            "04/06/2004", "117.556", "555256", "0022", 
            Setor.JURIDICO, 12, "5555"
        )

def test_verifica_salario_valor_advogado():
      with pytest.raises(ValueError, match= "O salario deve ser maior que zero"):
            Advogado(
            1, "Pedro", "55565", "pedro@", 
            Endereco("Rua a", "57", "térreo", "404560", "Salvador", UnidadeFederativa.BAHIA), 
            Sexo.MASCULINO, EstadoCivil.DIVORCIADO, 
            "04/06/2004", "117.556", "555256", "0022", 
            Setor.JURIDICO, -1500, "5555"
        )
           

    