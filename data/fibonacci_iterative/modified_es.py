def secuencia_fibonacci(numero_de_terminos):
    """
    Retorna una lista que contiene los primeros numeros numero_de_terminos
    de la secuencia Fibonacci utilizando un método iterativo
    """
    if numero_de_terminos <= 0:
        return []
    if numero_de_terminos == 1:
        return [0]

    secuencia = [0, 1]
    while len(secuencia) < numero_de_terminos:
        siguiente_termino = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente_termino)

    return secuencia


if __name__ == "__main__":
    contador = 10
    resultado = secuencia_fibonacci(contador)
    print(f"primeros {contador} numeros Fibonacci: {resultado}")
