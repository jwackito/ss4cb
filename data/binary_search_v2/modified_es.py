def busqueda_binaria(lista_ordenada, valor_objetivo):
    """
    Busca por el valor_objetivo en la lista_ordenada usand busqueda binaria.
    Retorna el indice de valor_objetivo si es encontrado, o -1 si no esta presente.
    """
    indice_izquierdo = 0
    indice_derecho = len(lista_ordenada) - 1

    while indice_izquierdo <= indice_derecho:
        indice_medio = (indice_izquierdo + indice_derecho) // 2
        valor_medio = lista_ordenada[indice_medio]

        if valor_medio == valor_objetivo:
            return indice_medio
        elif valor_medio < valor_objetivo:
            indice_izquierdo = indice_medio + 1
        else:
            indice_derecho = indice_medio - 1

    return -1


if __name__ == "__main__":
    numeros = [2, 5, 8, 12, 16, 23, 38, 45, 67, 90]
    objetivo = 23
    indice = binary_search(numeros, objetivo)
    if indice != -1:
        print(f"valor {objetivo} encontrado en indice {indice}")
    else:
        print(f"valor {objetivo} no encontrado")

