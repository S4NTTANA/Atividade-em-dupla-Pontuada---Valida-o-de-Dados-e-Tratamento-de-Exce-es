import pytest
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.setor import Setor
from projeto.models.enum.unidade_federativa import UnidadeFederativa

@pytest.fixture
def medico_exemplo():
    medico01 = Medico(
        1, "matheus", "55565", "pedro@", 
        Endereco("Rua a", "57", "térreo", "404560", "Salvador", UnidadeFederativa.BAHIA), 
        Sexo.MASCULINO, EstadoCivil.VIUVO, 
        "04/06/2004", "117.556", "555256", "0022", 
        Setor.JURIDICO, 1500.0, "5555"
    )
    return medico01


def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.id == 1

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.nome == "matheus"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.telefone == "55565"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.email == "pedro@"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.endereco.logradouro == "Rua a"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.endereco.numero == "57"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.endereco.complemento == "térreo"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.endereco.cep == "404560"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.endereco.cidade == "Salvador"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.endereco.uf == UnidadeFederativa.BAHIA

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.sexo == Sexo.MASCULINO

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.estadoCivil == EstadoCivil.VIUVO

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.dataNascimento == "04/06/2004"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.cpf == "117.556"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.rg == "555256"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.matricula == "0022"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.setor == Setor.JURIDICO

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.salario == 1500.0

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.crm == "5555"



def test_verifica_Id_tipo_advogado():
    with pytest.raises(TypeError, match="Digite um id valido"):
        Medico(
            "um", "matheus", "55565", "pedro@", 
            Endereco("Rua a", "57", "térreo", "404560", "Salvador", UnidadeFederativa.BAHIA), 
            Sexo.MASCULINO, EstadoCivil.VIUVO, 
            "04/06/2004", "117.556", "555256", "0022", 
            Setor.JURIDICO, 1500, "5555"
        )

def test_verifica_Id_negativo_advogado():
    with pytest.raises(ValueError, match="O id nao pode ser negativo"):
        Medico(
            -1, "matheus", "55565", "pedro@", 
            Endereco("Rua a", "57", "térreo", "404560", "Salvador", UnidadeFederativa.BAHIA), 
            Sexo.MASCULINO, EstadoCivil.VIUVO, 
            "04/06/2004", "117.556", "555256", "0022", 
            Setor.JURIDICO, 1500, "5555"
        )

def test_verifica_salario_tipo_advogado():
      with pytest.raises(TypeError, match= "Digite um salario valido"):
            Medico(
            1, "matheus", "55565", "pedro@", 
            Endereco("Rua a", "57", "térreo", "404560", "Salvador", UnidadeFederativa.BAHIA), 
            Sexo.MASCULINO, EstadoCivil.VIUVO, 
            "04/06/2004", "117.556", "555256", "0022", 
            Setor.JURIDICO, 12, "5555"
        )

def test_verifica_salario_valor_advogado():
      with pytest.raises(ValueError, match= "O salario deve ser maior que zero"):
            Medico(
            1, "matheus", "55565", "pedro@", 
            Endereco("Rua a", "57", "térreo", "404560", "Salvador", UnidadeFederativa.BAHIA), 
            Sexo.MASCULINO, EstadoCivil.VIUVO, 
            "04/06/2004", "117.556", "555256", "0022", 
            Setor.JURIDICO, -1500, "5555"
        )
           
    