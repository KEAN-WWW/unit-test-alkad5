import pytest
from src.calculator import div

def test_division():
    assert div(6, 2) == 3
    assert div(-10, 5) == -2

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)


