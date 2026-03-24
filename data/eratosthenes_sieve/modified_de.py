def eratosthenes_sieb(limit):
    """
    Das Sieb des Eratosthenes ist ein Algorithmus zur Bestimmung einer 
    Liste oder Tabelle aller Primzahlen kleiner oder gleich einer vorgegebenen Zahl.
    """
    ist_prim = [True] * (limit + 1)
    ist_prim[0] = False
    ist_prim[1] = False

    aktuelle_zahl = 2
    while aktuelle_zahl * aktuelle_zahl <= limit:
        if ist_prim[aktuelle_zahl]:
            vielfaches = aktuelle_zahl * aktuelle_zahl
            while vielfaches <= limit:
                ist_prim[vielfaches] = False
                vielfaches += aktuelle_zahl
        aktuelle_zahl += 1

    primzahl_liste = [nummer for nummer in range(2, limit + 1) if ist_prim[nummer]]
    return primzahl_liste


if __name__ == "__main__":
    obergrenze = 50
    ergebnis = eratosthenes_sieb(obergrenze)
    print(f"Primzahlen bis zur {obergrenze}: {ergebnis}")
