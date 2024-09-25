import pytest
from projeto.models.endereco import Endereco
from projeto.models.enum.unidade_federativa import UnidadeFederativa
from projeto.models.fornecedor import Fornecedor

@pytest.fixture
def fornecedor_valido():
    fornecedor01= Fornecedor (10,"Brama","+718889","Brama@",Endereco ("Rua A","57","Terrio","4047","Salvador",UnidadeFederativa.RIO_DE_JANEIRO),"741545","Bahia salvador","ferro")
    return fornecedor01

def test_id_negativo(fornecedor_valido):
    with pytest.raises (ValueError,match= "O id nao pode ser negativo"):
        Fornecedor (-10,"Brama","+718889","Brama@",Endereco ("Rua A","57","Terrio","4047","Salvador",UnidadeFederativa.RIO_DE_JANEIRO),"741545","Bahia salvador","ferro")
        
def test_id_valido(fornecedor_valido):
    assert fornecedor_valido.id == 10
      
def test_nome_valido(fornecedor_valido):
    assert fornecedor_valido.nome == "Brama"

def test_tell_valido(fornecedor_valido):
    assert fornecedor_valido.telefone == "+718889"

def test_email_valido(fornecedor_valido):
    assert fornecedor_valido.email == "Brama@"


def test_logradouro_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.logradouro == "Rua A"


def test_complemento_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.complemento == "Terrio"


def test_cep_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.cep == "4047"


def test_cidade_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.cidade == "Salvador"


def test_unidadeFederativa_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.uf == UnidadeFederativa.RIO_DE_JANEIRO


def test_cnph_valido(fornecedor_valido):
    assert fornecedor_valido.cnpj == "741545"

def test_inscricaoestadual_valido(fornecedor_valido):
    assert fornecedor_valido.inscricaoEstadual == "Bahia salvador"

def test_produto_valido(fornecedor_valido):
    assert fornecedor_valido.produto== "ferro"






