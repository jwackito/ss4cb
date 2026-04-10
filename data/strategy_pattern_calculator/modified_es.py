from abc import ABC, abstractmethod

# Interfaz de Estrategia
class OperacionMatematica(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

# Estrategia Concreta: Adicion
class Adicion(OperacionMatematica):
    def execute(self, a, b):
        return a + b

# Estrategia Concreta: Multiplicacion
class Multiplicacion(OperacionMatematica):
    def execute(self, a, b):
        return a * b

# Context Class
class Calculador:
    def __init__(self, estrategia: OperacionMatematica):
        self._estrategia = estrategia

    def set_estrategia(self, estrategia: OperacionMatematica):
        self._estrategia = estrategia

    def calcular(self, x, y):
        # Realizar la operacion utilizando la estrategia inyectada
        return self._estrategia.execute(x, y)

# Usage
if __name__ == "__main__":
    calc = Calculador(Adicion())
    print(f"Result: {calc.calcular(10, 5)}")