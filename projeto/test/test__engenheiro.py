import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.setor import Setor
from projeto.models.enum.unidade_federativa import UnidadeFederativa

@pytest.fixture
def medico_exemplo():
    engenheiro01 =Engenheiro(
        1, "matheus", "55565", "pedro@", 
        Endereco("Rua a", "57", "térreo", "404560", "rio de janeiro", UnidadeFederativa.RIO_DE_JANEIRO), 
        Sexo.FEMININO, EstadoCivil.DIVORCIADO, 
        "04/06/2004", "117.556", "555256", "0022", 
        Setor.SAUDE, 1500, "5555"
    )
    return engenheiro01


def test_verifica_Id_medico():
    with pytest.raises(TypeError, match="Digite um id valido"):
        Engenheiro(
            "um", "matheus", "55565", "pedro@", 
            Endereco("Rua a", "57", "térreo", "404560", "rio de janeiro", UnidadeFederativa.RIO_DE_JANEIRO), 
            Sexo.FEMININO, EstadoCivil.DIVORCIADO, 
            "04/06/2004", "117.556", "555256", "0022", 
            Setor.SAUDE, 1500, "5555"
        )
def test_verifica_salario_tipo_medico():
    with pytest.raises(TypeError, match= "Digite um salario valido"):
        Engenheiro(
            1, "matheus", "55565", "pedro@", 
            Endereco("Rua a", "57", "térreo", "404560", "rio de janeiro", UnidadeFederativa.RIO_DE_JANEIRO), 
            Sexo.FEMININO, EstadoCivil.DIVORCIADO, 
            "04/06/2004", "117.556", "555256", "0022", 
            Setor.SAUDE, 12, "5555"
        )

def test_verifica_salario_valor_medico():
    with pytest.raises(ValueError, match= "O salario deve ser maior que zero"):
     Engenheiro(
            1, "matheus", "55565", "pedro@", 
            Endereco("Rua a", "57", "térreo", "404560", "rio de janeiro", UnidadeFederativa.RIO_DE_JANEIRO), 
            Sexo.FEMININO, EstadoCivil.DIVORCIADO, 
            "04/06/2004", "117.556", "555256", "0022", 
            Setor.SAUDE, -1500, "5555"
        )
           
    