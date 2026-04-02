def ordenamiento_shell(arreglo):
    """Ordena una lista en orden ascendente usando el algoritmo de ordenamiento shell."""
    brecha = len(arreglo) // 2

    while brecha > 0:
        for indice_actual in range(brecha, len(arreglo)):
            valor_actual = arreglo[indice_actual]
            posicion = indice_actual

            while posicion >= brecha and arreglo[posicion - brecha] > valor_actual:
                arreglo[posicion] = arreglo[posicion - brecha]
                posicion -= brecha

            arreglo[posicion] = valor_actual

        brecha //= 2

    return arreglo