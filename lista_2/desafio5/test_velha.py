from velha import verificar_jogo


def test_vitoria_em_linha():
    tabuleiro = [
        ["X", "X", "X"],
        ["O", "O", ""],
        ["", "", ""],
    ]
    assert verificar_jogo(tabuleiro) == "venceu o X"


def test_vitoria_em_coluna():
    tabuleiro = [
        ["O", "X", ""],
        ["O", "X", ""],
        ["", "X", ""],
    ]
    assert verificar_jogo(tabuleiro) == "venceu o X"


def test_vitoria_na_diagonal_principal():
    tabuleiro = [
        ["X", "O", ""],
        ["O", "X", ""],
        ["", "", "X"],
    ]
    assert verificar_jogo(tabuleiro) == "venceu o X"


def test_vitoria_na_diagonal_secundaria():
    tabuleiro = [
        ["O", "O", "X"],
        ["O", "X", ""],
        ["X", "", ""],
    ]
    assert verificar_jogo(tabuleiro) == "venceu o X"


def test_empate():
    tabuleiro = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"],
    ]
    assert verificar_jogo(tabuleiro) == "empate"


def test_jogo_em_andamento():
    tabuleiro = [
        ["X", "", ""],
        ["", "O", ""],
        ["", "", ""],
    ]
    assert verificar_jogo(tabuleiro) == "em andamento"
