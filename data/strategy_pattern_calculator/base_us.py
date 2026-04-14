from abc import ABC, abstractmethod

# Strategy Interface
class MathOperation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

# Concrete Strategy: Addition
class Addition(MathOperation):
    def execute(self, a, b):
        return a + b

# Concrete Strategy: Multiplication
class Multiplication(MathOperation):
    def execute(self, a, b):
        return a * b

# Context Class
class Calculator:
    def __init__(self, strategy: MathOperation):
        self._strategy = strategy

    def set_strategy(self, strategy: MathOperation):
        self._strategy = strategy

    def calculate(self, x, y):
        # Perform the operation using the injected strategy
        return self._strategy.execute(x, y)

# Usage
if __name__ == "__main__":
    calc = Calculator(Addition())
    print(f"Result: {calc.calculate(10, 5)}")