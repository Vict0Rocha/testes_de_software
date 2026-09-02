import pytest

from calculadora_string import somar


def test_string_vazia_soma_zero():
    assert somar("") == 0


def test_um_numero_soma_ele_mesmo():
    assert somar("1") == 1


def test_varios_numeros_por_virgula_sao_somados():
    assert somar("1,2,3") == 6


def test_aceita_quebra_de_linha_como_separador():
    assert somar("1\n2,3") == 6


def test_aceita_separador_personalizado():
    assert somar("//;\n1;2") == 3


def test_numero_negativo_lanca_erro():
    with pytest.raises(ValueError):
        somar("1,-2,3")
