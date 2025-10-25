
from __future__ import annotations

def add(a: int | float, b: int | float) -> int | float:
    return a + b

def sub(a: int | float, b: int | float) -> int | float:
    return a - b

def mul(a: int | float, b: int | float) -> int | float:
    return a * b

def div(a: int | float, b: int | float) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


class Calculator:

    def add(self, a: int | float, b: int | float) -> int | float:
        return add(a, b)

    def sub(self, a: int | float, b: int | float) -> int | float:
        return sub(a, b)

    def mul(self, a: int | float, b: int | float) -> int | float:
        return mul(a, b)

    def div(self, a: int | float, b: int | float) -> float:
        return div(a, b)
