def calcular_total(itens, servico_de_precos):
    total = 0
    for item in itens:
        total += servico_de_precos.buscar_preco(item)
    return total
