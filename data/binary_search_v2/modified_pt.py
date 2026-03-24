def busca_binaria(lista_ordenada, valor_alvo):
    """
    Busca por valor_alvo em lista_ordenada utilizando busca binária.
    Retorna o índice de valor_alvo se encontrado, ou -1 se não presente.
    """
    indice_esquerdo = 0
    indice_direito = len(lista_ordenada) - 1

    while indice_esquerdo <= indice_direito:
        indice_meio = (indice_esquerdo + indice_direito) // 2
        valor_meio = lista_ordenada[indice_meio]

        if valor_meio == valor_alvo:
            return indice_meio
        elif valor_meio < valor_alvo:
            indice_esquerdo = indice_meio + 1
        else:
            indice_direito = indice_meio - 1

    return -1


if __name__ == "__main__":
    numeros = [2, 5, 8, 12, 16, 23, 38, 45, 67, 90]
    alvo = 23
    indice = busca_binaria(numeros, alvo)
    if indice != -1:
        print(f"valor {alvo} encontrado no indice {indice}")
    else:
        print(f"valor {alvo} não encontrado")
