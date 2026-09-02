import pytest

from calculadora_rpn import calcular_rpn


def test_numero_unico_devolve_ele_mesmo():
    assert calcular_rpn("3") == 3


def test_soma_de_dois_numeros():
    assert calcular_rpn("3 4 +") == 7


def test_subtracao_de_dois_numeros():
    assert calcular_rpn("10 4 -") == 6


def test_multiplicacao_de_dois_numeros():
    assert calcular_rpn("3 4 *") == 12


def test_divisao_de_dois_numeros():
    assert calcular_rpn("10 2 /") == 5


def test_varias_operacoes_encadeadas():
    assert calcular_rpn("5 1 2 + 4 * + 3 -") == 14


def test_divisao_por_zero_lanca_erro():
    with pytest.raises(ZeroDivisionError):
        calcular_rpn("5 0 /")


def test_expressao_malformada_lanca_erro():
    with pytest.raises(ValueError):
        calcular_rpn("1 +")
