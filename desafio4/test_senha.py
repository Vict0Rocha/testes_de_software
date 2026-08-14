import pytest

from senha import senha_forte

'''
O @pytest.mark.parametrize é um decorador que roda a mesma função de teste
várias vezes, uma para cada linha da lista, trocando os valores de senha e esperado.
'''
@pytest.mark.parametrize("senha, esperado", [
    ("Abc12345", True),      # tem maiuscula, numero e 8 caracteres
    ("abcdefgh", False),     # sem maiuscula
    ("ABCDEFGH", False),     # sem numero
    ("Abc123", False),       # menos de 8 caracteres
    ("", False),             # vazia
])
def test_senha_forte(senha, esperado):
    assert senha_forte(senha) == esperado


def test_senha_passa_no_teste_mas_ainda_e_fraca():
    # essa senha passa na nossa regra (maiuscula + numero + 8 caracteres),
    # mas "Senha123" e uma senha bem obvia e facil de adivinhar.
    # isso mostra que passar no teste nao prova que a funcao esta livre de
    # defeitos: a nossa regra nao verifica senhas comuns/previsiveis.
    assert senha_forte("Senha123") is True
