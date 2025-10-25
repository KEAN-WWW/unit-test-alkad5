import pytest
from src.calculator import Calculator

calc = Calculator()

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.div(7, 0)

