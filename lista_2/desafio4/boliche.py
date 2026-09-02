def calcular_pontuacao(jogadas):
    pontuacao = 0
    i = 0

    for frame in range(10):
        if jogadas[i] == 10:
            pontuacao += 10 + jogadas[i + 1] + jogadas[i + 2]
            i += 1
        elif jogadas[i] + jogadas[i + 1] == 10:
            pontuacao += 10 + jogadas[i + 2]
            i += 2
        else:
            pontuacao += jogadas[i] + jogadas[i + 1]
            i += 2

    return pontuacao
