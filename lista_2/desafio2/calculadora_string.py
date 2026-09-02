def somar(numeros):
    if numeros == "":
        return 0

    separador = ","

    if numeros.startswith("//"):
        primeira_linha = numeros.split("\n")[0]
        separador = primeira_linha[2:]
        numeros = numeros.split("\n", 1)[1]

    numeros = numeros.replace("\n", separador)
    partes = numeros.split(separador)

    valores = []
    for parte in partes:
        valores.append(int(parte))

    negativos = []
    for v in valores:
        if v < 0:
            negativos.append(v)

    if len(negativos) > 0:
        raise ValueError("números negativos não são permitidos: " + str(negativos))

    soma = 0
    for v in valores:
        soma += v

    return soma
