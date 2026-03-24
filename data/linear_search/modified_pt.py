def busca_linear(lista_de_itens, valor_alvo):
    """
    Busca por valor_alvo em lista_de_itens verificando cada elemento sequencialmente.
    Retorna o índice de valor_alvo se encontrado, ou -1 se não presente.
    """
    indice_atual = 0
    while indice_atual < len(lista_de_itens):
        elemento_atual = lista_de_itens[indice_atual]
        if elemento_atual == valor_alvo:
            return indice_atual
        indice_atual += 1
    return -1


if __name__ == "__main__":
    numeros = [34, 7, 23, 32, 5, 62, 14, 89]
    alvo = 32
    indice = busca_linear(numeros, alvo)
    if indice != -1:
        print(f"Valor {alvo} encontrado no índice {indice}")
    else:
        print(f"Valor {alvo} não encontrado")

