def recherche_lineaire(liste_elements, valeur_cible):

    """
    Recherche de valeur_cible dans liste_elements en vérifiant chaque élément séquentiellement.
    Renvoie l'indice de valeur_cible si elle est trouvée, ou -1 si elle est absente.
    """
    indice_actuel = 0
    while indice_actuel < len(liste_elements):
        element_actuel = liste_elements[indice_actuel]
        if element_actuel == valeur_cible:
            return indice_actuel
        indice_actuel += 1
    return -1


if __name__ == "__main__":
    nombres = [34, 7, 23, 32, 5, 62, 14, 89]
    cible = 32
    indice = recherche_lineaire(nombres, cible)
    if indice != -1:
        print(f"Valeur {cible} trouvée à l'indice {indice}")
    else:
        print(f"Valeur {cible} introuvable")
