def euklidischer_ggT(erste_Zahl, zweite_Zahl):
    """
    Gibt den größten gemeinsamen Teiler von erste_Zahl und zweite_Zahl zurück.
    unter Verwendung des euklidischen Algorithmus.
    """
    dividende = erste_Zahl
    divisor = zweite_Zahl

    while divisor != 0:
        rest = dividende % divisor
        dividende = divisor
        divisor = rest

    return dividende


if __name__ == "__main__":
    nummer_a = 48
    nummer_b = 18
    ergebnis = euklidischer_ggT(nummer_a, nummer_b)
    print(f"Der größte gemeinsame Teiler von {nummer_a} und {nummer_b} ist: {ergebnis}")
