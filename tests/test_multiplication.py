from src.calculator import mul

def test_multiplication():
    assert mul(2, 3) == 6
    assert mul(0, 100) == 0
    assert mul(-2, 3) == -6

