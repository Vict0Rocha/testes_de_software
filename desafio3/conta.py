def sacar(saldo, valor):
    if valor <= 0:
        raise ValueError("o valor do saque deve ser maior que zero")
    if valor > saldo:
        raise ValueError("saldo insuficiente")
    return saldo - valor
