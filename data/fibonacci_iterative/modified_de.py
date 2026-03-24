def fibonacci_iterativ(anzahl_der_elemente):
    """
    Die Fibonacci-Folge ist die unendliche Folge natürlicher Zahlen, 
    die mit zweimal der Zahl 1 beginnt und bei der jede weitere Zahl die 
    Summe der beiden ihr vorangehenden Zahlen ist
    """
    if anzahl_der_elemente <= 0:
        return []
    if anzahl_der_elemente == 1:
        return [0]

    sequenz = [0, 1]
    while len(sequenz) < anzahl_der_elemente:
        naechster_glied = sequenz[-1] + sequenz[-2]
        sequenz.append(naechster_glied)

    return sequenz


if __name__ == "__main__":
    zaehlen = 10
    ergebnis = fibonacci_iterativ(zaehlen)
    print(f"Erste {zaehlen} Fibonacci-Zahlen: {ergebnis}")
