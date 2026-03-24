def crivello_Di_Eratostene(limite):
    """
    Il crivello di Eratostene è un antico algoritmo per 
    il calcolo dei numeri primi fino a un certo numero prefissato
    """
    e_primo = [True] * (limite + 1)
    e_primo[0] = False
    e_primo[1] = False

    numero_attuale = 2
    while numero_attuale * numero_attuale <= limite:
        if e_primo[numero_attuale]:
            multiplo = numero_attuale * numero_attuale
            while multiplo <= limite:
                e_primo[multiplo] = False
                multiplo += numero_attuale
        numero_attuale += 1

    lista_dei_primi = [numero for numero in range(2, limite + 1) if e_primo[numero]]
    return lista_dei_primi


if __name__ == "__main__":
    limite_superiore = 50
    risultato = crivello_Di_Eratostene(limite_superiore)
    print(f"Numeri primi fino a {limite_superiore}: {risultato}")
