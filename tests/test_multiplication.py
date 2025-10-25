import pytest
from src.calculator import Calculator

calc = Calculator()

def test_multiplication():
    assert calc.mul(6, 4) == 24
