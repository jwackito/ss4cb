def crible_d_Eratosthene(limite):
    """
    Renvoie la liste de tous les nombres premiers jusqu'à limite inclus
    en utilisant l'algorithme du crible d'Ératosthène.
    """
    est_premier = [True] * (limite + 1)
    est_premier[0] = False
    est_premier[1] = False

    numero_actuel = 2
    while numero_actuel * numero_actuel <= limite:
        if est_premier[numero_actuel]:
            multiple = numero_actuel * numero_actuel
            while multiple <= limite:
                est_premier[multiple] = False
                multiple += numero_actuel
        numero_actuel += 1

    nombres_premiers = [nombre for nombre in range(2, limite + 1) if est_premier[nombre]]
    return nombres_premiers


if __name__ == "__main__":
    limite_superieure = 50
    resultat = crible_d_Eratosthene(limite_superieure)
    print(f"Premiers nombres jusqu'à {limite_superieure}: {resultat}")
