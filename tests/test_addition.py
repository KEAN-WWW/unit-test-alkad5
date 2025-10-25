from src.calculator import Calculator

calc = Calculator()

def test_addition():
    assert calc.add(4, 3) == 7
    assert calc.add(-1, 4) == 3
