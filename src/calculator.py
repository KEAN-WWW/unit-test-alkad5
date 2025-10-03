# src/calculator.py

def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

def mul(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

class Calculator:
    def add(self, a: int, b: int) -> int:  return add(a, b)
    def sub(self, a: int, b: int) -> int:  return sub(a, b)
    def mul(self, a: int, b: int) -> int:  return mul(a, b)
    def div(self, a: int, b: int) -> float:return div(a, b)
