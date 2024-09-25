import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.setor import Setor
from projeto.models.enum.unidade_federativa import UnidadeFederativa

@pytest.fixture
def engenheiro_exemplo():
    engenheiro01 = Engenheiro(
        1, "matheus", "55565", "pedro@", 
        Endereco("Rua a", "57", "térreo", "404560", "rio de janeiro", UnidadeFederativa.RIO_DE_JANEIRO), 
        Sexo.FEMININO, EstadoCivil.DIVORCIADO, 
        "04/06/2004", "117.556", "555256", "0022", 
        Setor.SAUDE, 1500.0, "5555"
    )
    return engenheiro01


def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.id == 1

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.nome == "matheus"

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.telefone == "55565"

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.email == "pedro@"

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.endereco.logradouro == "Rua a"

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.endereco.numero == "57"

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.endereco.complemento == "térreo"

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.endereco.cep == "404560"

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.endereco.cidade == "rio de janeiro"

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.endereco.uf == UnidadeFederativa.RIO_DE_JANEIRO

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.sexo == Sexo.FEMININO

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.estadoCivil == EstadoCivil.DIVORCIADO

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.dataNascimento == "04/06/2004"

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.cpf == "117.556"

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.rg == "555256"

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.matricula == "0022"

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.setor == Setor.SAUDE

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.salario == 1500.0

def test_engenheiro_exemplo(engenheiro_exemplo):
    assert engenheiro_exemplo.crea == "5555"


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
           
    