def ordenar_por_insercion(arreglo):
    """Ordena una lista en orden ascendente usando el algoritmo de ordenamiento por inserción."""
    for indice_actual in range(1, len(arreglo)):
        valor_actual = arreglo[indice_actual]
        posicion = indice_actual - 1

        while posicion >= 0 and arreglo[posicion] > valor_actual:
            arreglo[posicion + 1] = arreglo[posicion]
            posicion -= 1

        arreglo[posicion + 1] = valor_actual

    return arreglo