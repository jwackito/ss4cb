def mdc_euclidiano(primeiro_numero, segundo_numero):
    """
    Retorna o máximo divisor comum de primeiro_numero e segundo_numero
    utilizando o algoritmo de Euclides.
    """
    dividendo = primeiro_numero
    divisor = segundo_numero

    while divisor != 0:
        resto = dividendo % divisor
        dividendo = divisor
        divisor = resto

    return dividendo


if __name__ == "__main__":
    numero_a = 48
    numero_b = 18
    resultado = mdc_euclidiano(numero_a, numero_b)
    print(f"MDC de {numero_a} e {numero_b} é: {resultado}")
