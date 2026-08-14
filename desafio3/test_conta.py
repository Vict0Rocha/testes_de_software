import pytest

from conta import sacar


def test_saque_valido():
    assert sacar(100, 40) == 60


def test_saque_maior_que_saldo_lanca_erro():
    with pytest.raises(ValueError):
        sacar(100, 150)


def test_saque_de_valor_negativo_lanca_erro():
    with pytest.raises(ValueError):
        sacar(100, -10)
