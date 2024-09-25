import pytest
from projeto.models.endereco import Endereco
from projeto.models.enum.unidade_federativa import UnidadeFederativa
from projeto.models.cliente import Cliente
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.estadoCivil import EstadoCivil

@pytest.fixture 
def cliente_valido():
    cliente1 = Cliente(456789, "Faustao", "4002", "faustin@gmail.com", Endereco("Rua A", "55", "casa", "4556", "Salvador", UnidadeFederativa.BAHIA),
                       Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "25/12/2000", 8922)
    return cliente1

def test_cliente_valido(cliente_valido):
    assert cliente_valido.id == 456789

def test_cliente_valido(cliente_valido):
    assert cliente_valido.nome == "Faustao"

def test_cliente_valido(cliente_valido):
    assert cliente_valido.telefone == "4002"

def test_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.logradouro == "Rua A"

def test_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.numero == "55"

def test_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.complemento == "casa"

def test_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.cep == "4556"

def test_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.cidade == "Salvador"

def test_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_cliente_valido(cliente_valido):
    assert cliente_valido.sexo == Sexo.MASCULINO

def test_cliente_valido(cliente_valido):
    assert cliente_valido.estadoCivil == EstadoCivil.SOLTEIRO

def test_cliente_valido(cliente_valido):
    assert cliente_valido.dataNascimento == "25/12/2000"

def test_cliente_valido(cliente_valido):
    assert cliente_valido.protocolo == 8922

