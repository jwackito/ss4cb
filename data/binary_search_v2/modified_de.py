def binaere_suche(sortierte_liste, gesuchter_wert):
    """
    Sucht mithilfe der binären Suche nach gesuchter_wert in sortierte_liste.
    Gibt den Index von gesuchter_wert zurück, falls dieser gefunden wurde, andernfalls -1.
    """
    links_index = 0
    rechts_index = len(sortierte_liste) - 1

    while links_index <= rechts_index:
        mitte_index = (links_index + rechts_index) // 2
        mitte_wert = sortierte_liste[mitte_index]

        if mitte_wert == gesuchter_wert:
            return mitte_index
        elif mitte_wert < gesuchter_wert:
            links_index = mitte_index + 1
        else:
            rechts_index = mitte_index - 1

    return -1


if __name__ == "__main__":
    zahlen = [2, 5, 8, 12, 16, 23, 38, 45, 67, 90]
    gesuchter = 23
    index = binäre_suche(zahlen, gesuchter)
    if index != -1:
        print(f"wert {gesuchter} gefunden bei index {index}")
    else:
        print(f"Wert {gesuchter} nicht gefunden")

