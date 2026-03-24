def pgcd_euclidien(premier_nombre, deuxieme_nombre):


    """
    Renvoie le plus grand commun diviseur de premier_nombre et deuxième_nombre
    en utilisant l'algorithme d'Euclide.

    """
    dividende = premier_nombre
    diviseur = deuxieme_nombre

    while diviseur != 0:
        reste = dividende % diviseur
        dividende = diviseur
        diviseur = reste

    return dividende


if __name__ == "__main__":
    nombre_a = 48
    nombre_b = 18
    resultat = pgcd_euclidien(nombre_a, num_b)
    print(f"Le PGCD de {nombre_a} et {num_b} est : {resultat}")
