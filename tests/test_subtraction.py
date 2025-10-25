from src.calculator import Calculator

calc = Calculator()

def test_subtraction():
    assert calc.sub(6, 2) == 4
    assert calc.sub(2, 5) == -3
