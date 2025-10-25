"""Basic arithmetic functions used by unit tests."""

def add(num_a: float, num_b: float) -> float:
    """Return the sum of two numbers."""
    return num_a + num_b

def sub(num_a: float, num_b: float) -> float:
    """Return the difference num_a - num_b."""
    return num_a - num_b

def mul(num_a: float, num_b: float) -> float:
    """Return the product of two numbers."""
    return num_a * num_b

def div(num_a: float, num_b: float) -> float:
    """Return the quotient num_a / num_b; raise on divide-by-zero."""
    if num_b == 0:
        raise ZeroDivisionError("division by zero")
    return num_a / num_b


