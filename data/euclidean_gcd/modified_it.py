def gcd_euclideo(primo_numero, secondo_numero):
    """
    Restituisce il massimo comun divisore di primo_numero e secondo_numero
    utilizzando l'algoritmo euclideo.
    """
    dividendo = primo_numero
    divisore = secondo_numero

    while divisore != 0:
        resto = dividendo % divisore
        dividendo = divisore
        divisore = resto

    return dividendo


if __name__ == "__main__":
    numero_a = 48
    numero_b = 18
    risultato = gcd_euclideo(numero_a, numero_b)
    print(f"Il MCD di {numero_a} e {numero_b} è: {risultato}")
