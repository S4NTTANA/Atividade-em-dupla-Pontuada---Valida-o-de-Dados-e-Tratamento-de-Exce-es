import pytest
from projeto.models.endereco import Endereco
from projeto.models.enum.unidade_federativa import UnidadeFederativa
from projeto.models.prestacaodeServico import Prestacaodeservicos
@pytest.fixture
def pretacao_valida():
    prestacao01= Prestacaodeservicos(10,"Brama","+718889","Brama@",
                                    Endereco ("Rua A","57","Terrio","4047","Salvador",UnidadeFederativa.SAO_PAULO),"4441","bahia","10-02","10-08")
    return prestacao01

def test_id_negativo(pretacao_valida):
    with pytest.raises (ValueError,match= "O id nao pode ser negativo"):
        Prestacaodeservicos(-10,"Brama","+718889","Brama@",
                            Endereco ("Rua A","57","Terrio","4047","Salvador",UnidadeFederativa.SAO_PAULO),"4441","bahia","10-02","10-2")

def test_id_tipo_prestacao_de_servicos(pretacao_valida):
    with pytest.raises (TypeError,match= "Digite um id valido"):
        Prestacaodeservicos("10","Brama","+718889","Brama@",
                            Endereco ("Rua A","57","Terrio","4047","Salvador",UnidadeFederativa.SAO_PAULO),"4441","bahia","10-02","10-2")

def test_id_valido(pretacao_valida):
    assert pretacao_valida.id == 10
      
def test_nome_valido(pretacao_valida):
    assert pretacao_valida.nome == "Brama"

def test_tell_valido(pretacao_valida):
    assert pretacao_valida.telefone == "+718889"

def test_email_valido(pretacao_valida):
    assert pretacao_valida.email == "Brama@"


def test_logradouro_valido(pretacao_valida):
    assert pretacao_valida.endereco.logradouro == "Rua A"


def test_complemento_valido(pretacao_valida):
    assert pretacao_valida.endereco.complemento == "Terrio"


def test_cep_valido(pretacao_valida):
    assert pretacao_valida.endereco.cep == "4047"


def test_cidade_valido(pretacao_valida):
    assert pretacao_valida.endereco.cidade == "Salvador"


def test_unidadeFederativa_valido(pretacao_valida):
    assert pretacao_valida.endereco.uf == UnidadeFederativa.SAO_PAULO


def test_cnph_valido(pretacao_valida):
    assert pretacao_valida.cnpj == "4441"

def test_inscricaoestadual_valido(pretacao_valida):
    assert pretacao_valida.inscricaoEstadual == "bahia"

def test_contratoinicio_valido(pretacao_valida):
    assert pretacao_valida.contratoInicio == "10-02"

def test_contratofim_valido(pretacao_valida):
    assert pretacao_valida.contratoFim == "10-08"







