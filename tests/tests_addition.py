"""Unit tests for the add() function."""

from src.calculator import add

def test_addition():
    """Tests addition with positive, negative, and zero values."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
