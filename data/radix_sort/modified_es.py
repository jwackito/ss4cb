def ordenamiento_por_conteo_de_digitos(arreglo, posicion_digito):
    """Ordena el arreglo basado en el digito en el lugar del valor recibido."""
    tamano = len(arreglo)
    salida = [0] * tamano
    cantidad_digito = [0] * 10

    for numero in arreglo:
        digito = (numero // posicion_digito) % 10
        cantidad_digito[digito] += 1

    for i in range(1, 10):
        cantidad_digito[i] += cantidad_digito[i - 1]

    for i in range(tamano - 1, -1, -1):
        digito = (arreglo[i] // posicion_digito) % 10
        salida[cantidad_digito[digito] - 1] = arreglo[i]
        cantidad_digito[digito] -= 1

    for i in range(tamano):
        arreglo[i] = salida[i]


def ordenamiento_radix(arreglo):
    """Ordena una lista de enteros no negativos usando el algoritmo de ordenamiento radix."""
    valor_maximo = max(arreglo)
    posicion_digito = 1

    while valor_maximo // posicion_digito > 0:
        ordenamiento_por_conteo_de_digitos(arreglo, posicion_digito)
        posicion_digito *= 10

    return arreglo