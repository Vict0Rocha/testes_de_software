def calcular_rpn(expressao):
    pilha = []
    tokens = expressao.split()

    for token in tokens:
        if token == "+" or token == "-" or token == "*" or token == "/":
            if len(pilha) < 2:
                raise ValueError("expressão inválida")

            b = pilha.pop()
            a = pilha.pop()

            if token == "+":
                resultado = a + b
            elif token == "-":
                resultado = a - b
            elif token == "*":
                resultado = a * b
            else:
                if b == 0:
                    raise ZeroDivisionError("divisão por zero")
                resultado = a / b

            pilha.append(resultado)
        else:
            pilha.append(float(token))

    if len(pilha) != 1:
        raise ValueError("expressão inválida")

    return pilha[0]
