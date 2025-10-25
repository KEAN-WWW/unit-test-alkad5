import pytest
from src.calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(2, 3) == 5

def test_sub():
    assert calc.sub(5, 2) == 3

def test_mul():
    assert calc.mul(3, 4) == 12

def test_div():
    assert calc.div(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.div(5, 0)

def test_divide_zero_exception_function():
    with pytest.raises(ZeroDivisionError):
        divide_zero_exception()
