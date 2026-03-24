def fibonacci_iterativo(numero_de_termos):
    """
    Retorna uma lista contendo os primeiros números de numero_de_termos
    da sequência de Fibonacci usando uma abordagem iterativa.
    """
    if numero_de_termos <= 0:
        return []
    if numero_de_termos == 1:
        return [0]

    sequencia = [0, 1]
    while len(sequencia) < numero_de_termos:
        proximo_termo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_termo)

    return sequencia


if __name__ == "__main__":
    contagem = 10
    resultado = fibonacci_iterativo(contagem)
    print(f"Primeiros {contagem} Números de Fibonacci: {resultado}")

