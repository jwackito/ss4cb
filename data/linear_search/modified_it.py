def ricerca_lineare(lista_articoli, valore_obiettivo):
    """
    Cerca valore_obiettivo in lista_articoli controllando ogni elemento in sequenza.
    Restituisce l'indice di valore_obiettivo se trovato, altrimenti -1.
    """
    indice_attuale = 0
    while indice_attuale < len(lista_articoli):
        elemento_attuale = lista_articoli[indice_attuale]
        if elemento_attuale == valore_obiettivo:
            return indice_attuale
        indice_attuale += 1
    return -1


if __name__ == "__main__":
    numeri = [34, 7, 23, 32, 5, 62, 14, 89]
    bersaglio = 32
    indice = ricerca_lineare(numeri, bersaglio)
    if indice != -1:
        print(f"Valore {bersaglio} trovato all'indice {indice}")
    else:
        print(f"Valore {bersaglio} non trovato")

