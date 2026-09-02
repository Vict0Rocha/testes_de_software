def situacao_aluno(nota):
    if nota < 6:
        return "reprovado"
    elif nota < 7:
        return "recuperacao"
    else:
        return "aprovado"
