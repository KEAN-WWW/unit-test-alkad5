"""Unit tests for the mul() function."""

from src.calculator import mul

def test_multiplication():
    """Tests multiplication with positive, negative, and zero values."""
    assert mul(2, 3) == 6
    assert mul(0, 100) == 0
    assert mul(-2, 3) == -6
