import pytest

from romano import numero_para_romano


@pytest.mark.parametrize("numero, esperado", [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (5, "V"),
    (6, "VI"),
    (10, "X"),
    (30, "XXX"),
    (4, "IV"),
    (9, "IX"),
    (40, "XL"),
    (90, "XC"),
    (400, "CD"),
    (900, "CM"),
    (50, "L"),
    (100, "C"),
    (500, "D"),
    (1000, "M"),
    (58, "LVIII"),
    (1994, "MCMXCIV"),
    (3999, "MMMCMXCIX"),
])
def test_numero_para_romano(numero, esperado):
    assert numero_para_romano(numero) == esperado
