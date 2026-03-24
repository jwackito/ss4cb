def fibonacci_iterativo(numero_termini):
    """
    Restituisce un lista contenente i primi numeri di termine
    della successione di Fibonacci utilizzando un approccio iterativo.
    """
    if numero_termini <= 0:
        return []
    if numero_termini == 1:
        return [0]

    successione = [0, 1]
    while len(successione) < numero_termini:
        prossimo_termine = successione[-1] + successione[-2]
        successione.append(prossimo_termine)

    return successione


if __name__ == "__main__":
    quantita = 10
    risultato = fibonacci_iterativo(quantita)
    print(f"Primi {quantita} numeri di Fibonacci: {risultato}")
