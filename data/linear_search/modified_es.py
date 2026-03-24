def busqueda_lineal(lista_de_elementos, valor_objetivo):
    """
    Busco por valor_objetivo en la lista de elementos evaluando cada elemento secuencialmente
    Retorna el indice del valor_objetivo si lo encontro o -1 si no esta presente.
    """
    indice_actual = 0
    while indice_actual < len(lista_de_elementos):
        elemento_actual = lista_de_elementos[indice_actual]
        if elemento_actual == valor_objetivo:
            return indice_actual
        indice_actual += 1
    return -1


if __name__ == "__main__":
    numeros = [34, 7, 23, 32, 5, 62, 14, 89]
    objetivo = 32
    indice = busqueda_lineal(numeros, objetivo)
    if indice != -1:
        print(f"Valor {objetivo} encontrado en indice {indice}")
    else:
        print(f"Valor {objetivo} no encontrado")
