from par_ou_impar import par_ou_impar


def test_numero_par():
    assert par_ou_impar(4) == "par"


def test_numero_impar():
    assert par_ou_impar(7) == "impar"


def test_numero_zero():
    assert par_ou_impar(0) == "par"
