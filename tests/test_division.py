"""Unit tests for the div() function."""

import pytest
from src.calculator import div

def test_division():
    """Tests division with positive and negative values."""
    assert div(6, 2) == 3
    assert div(-10, 5) == -2

def test_division_by_zero():
    """Tests that dividing by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        div(5, 0)
