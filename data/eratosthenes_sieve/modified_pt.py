def crivo_de_eratostenes(limite):
    """
    O Crivo de Eratóstenes é um algoritmo e um método simples e
    prático para encontrar números primos até um certo valor limite. 
    """
    e_primo = [True] * (limite + 1)
    e_primo[0] = False
    e_primo[1] = False

    numero_atual = 2
    while numero_atual * numero_atual <= limite:
        if e_primo[numero_atual]:
            multiplo = numero_atual * numero_atual
            while multiplo <= limite:
                e_primo[multiplo] = False
                multiplo += numero_atual
        numero_atual += 1

    lista_primos = [numero for numero in range(2, limite + 1) if e_primo[numero]]
    return lista_primos


if __name__ == "__main__":
    limite_superior = 50
    resultado = crivo_de_eratostenes(limite_superior)
    print(f"Números primos até {limite_superior}: {resultado}")
