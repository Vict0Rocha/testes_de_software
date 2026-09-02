def numero_para_romano(numero):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    texto = ""
    for i in range(len(valores)):
        while numero >= valores[i]:
            texto += simbolos[i]
            numero -= valores[i]

    return texto
