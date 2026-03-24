def fibonacci_iteratif(nombre_de_termes):

    """
    la suite de Fibonacci, tirant son nom du mathématicien 
    italien Fibonacci, est une suite de nombres entiers dans laquelle chaque 
    nombre est la somme des deux nombres qui le précèdent.
    """
    if nombre_de_termes <= 0:
        return []
    if nombre_de_termes == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < nombre_de_termes:
        terme_suivant = sequence[-1] + sequence[-2]
        sequence.append(terme_suivant)

    return sequence


if __name__ == "__main__":
    nombre = 10
    resultat = fibonacci_iteratif(nombre)
    print(f"les premiers {nombre} Les nombres de Fibonacci: {resultat}")
