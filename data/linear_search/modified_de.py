def lineare_suche(artikel_liste, ziel_wert):
    """
    Sucht in der Artikelliste nach „ziel_wert“, indem jedes Element nacheinander geprüft wird.
    Gibt den Index von „ziel_wert“ zurück, falls gefunden, andernfalls -1.
    """
    aktueller_index = 0
    while aktueller_index < len(artikel_liste):
        aktuelles_element = artikel_liste[aktueller_index]
        if aktuelles_element == ziel_wert:
            return aktueller_index
        aktueller_index += 1
    return -1


if __name__ == "__main__":
    zahlen = [34, 7, 23, 32, 5, 62, 14, 89]
    ziel = 32
    index = lineare_suche(zahlen, ziel)
    if index != -1:
        print(f"Wert {ziel} gefunden im Index {index}")
    else:
        print(f"Wert {ziel} nicht gefunden")
