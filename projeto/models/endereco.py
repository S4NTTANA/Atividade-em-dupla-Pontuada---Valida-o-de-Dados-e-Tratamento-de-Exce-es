from projeto.models.enum import unidade_federativa

class Endereco():
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: unidade_federativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCep: {self.cep}"
            f"\nCidade: {self.cidade}"
            f"\nUnidade Federativa: {self.uf}"
        )