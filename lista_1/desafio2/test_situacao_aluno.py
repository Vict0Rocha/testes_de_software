from situacao_aluno import situacao_aluno


def test_nota_abaixo_do_limite_reprovado():
    assert situacao_aluno(5.9) == "reprovado"


def test_nota_no_limite_reprovado():
    assert situacao_aluno(6) == "recuperacao"


def test_nota_abaixo_do_limite_recuperacao():
    assert situacao_aluno(6.9) == "recuperacao"


def test_nota_no_limite_aprovado():
    assert situacao_aluno(7) == "aprovado"


def test_nota_alta_aprovado():
    assert situacao_aluno(10) == "aprovado"
