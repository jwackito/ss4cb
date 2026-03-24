def mcd_euclideas(primero_numero, segundo_numero):
    """
    Retorna el mayor comun divisor del primer y segund numero
    usando el algoritmo euclideo
    """
    dividendo = primero_numero
    divisor = segundo_numero

    while divisor != 0:
        resto = dividendo % divisor
        dividendo = divisor
        divisor = resto

    return dividendo


if __name__ == "__main__":
    num_a = 48
    num_b = 18
    resultado = mcd_euclideas(num_a, num_b)
    print(f"GCD de {num_a} y {num_b} es: {resultado}")
