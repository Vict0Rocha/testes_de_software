def verificar_jogo(tabuleiro):
    linhas = tabuleiro

    colunas = []
    for c in range(3):
        coluna = [tabuleiro[0][c], tabuleiro[1][c], tabuleiro[2][c]]
        colunas.append(coluna)

    diagonal1 = [tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]]
    diagonal2 = [tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]]

    todas_as_linhas = linhas + colunas + [diagonal1, diagonal2]

    for linha in todas_as_linhas:
        if linha[0] != "" and linha[0] == linha[1] and linha[1] == linha[2]:
            return "venceu o " + linha[0]

    tem_casa_vazia = False
    for linha in tabuleiro:
        for casa in linha:
            if casa == "":
                tem_casa_vazia = True

    if tem_casa_vazia:
        return "em andamento"

    return "empate"
