def ricerca_dicotomica(lista_ordinata, valore_bersaglio):
    """
    Cerca valore_bersaglio in lista_ordinata utilizzando la ricerca binaria.
    Restituisce l'indice di valore_bersaglio se trovato, altrimenti -1.
    """
    indice_sinistro = 0
    indice_destro = len(lista_ordinata) - 1

    while indice_sinistro <= indice_destro:
        indice_mezzo = (indice_sinistro + indice_destro) // 2
        valore_mezzo = lista_ordinata[indice_mezzo]

        if valore_mezzo == valore_bersaglio:
            return indice_mezzo
        elif valore_mezzo < valore_bersaglio:
            indice_sinistro = indice_mezzo + 1
        else:
            indice_destro = indice_mezzo - 1

    return -1


if __name__ == "__main__":
    numeri = [2, 5, 8, 12, 16, 23, 38, 45, 67, 90]
    bersaglio = 23
    indice = ricerca_dicotomica(numeri, bersaglio)
    if indice != -1:
        print(f"valore {bersaglio} trovato all'indice {indice}")
    else:
        print(f"valore {bersaglio} non trovato")
