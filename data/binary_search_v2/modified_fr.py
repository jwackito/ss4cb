def recherche_dichotomique(liste_triee, valeur_cible):
    """
    Recherche de cible_valeur dans liste_triee en utilisant une recherche binaire.
    Renvoie l'indice de cible_valeur s'il est trouvé, ou -1 s'il est absent.
    """
    indice_gauche = 0
    indice_droite = len(liste_triee) - 1 

    while indice_gauche <= indice_droite:
        milieu_indice = (indice_gauche + indice_droite) // 2
        milieu_valeur = liste_triee[milieu_indice]

        if milieu_valeur == valeur_cible:
            return milieu_indice
        elif milieu_valeur < valeur_cible:
            indice_gauche = milieu_indice + 1
        else:
            indice_droite = milieu_indice - 1

    return -1


if __name__ == "__main__":
    nombres = [2, 5, 8, 12, 16, 23, 38, 45, 67, 90]
    cible = 23
    indice = recherche_dichotomique(nombres, cible)
    if indice != -1:
        print(f"valeur {cible} trouvée à l'indice {indice}")
    else:
        print(f"valeur {cible} introuvable")

