from src.calculator import sub

def test_subtraction():
    assert sub(5, 3) == 2
    assert sub(0, 5) == -5
    assert sub(-1, -1) == 0



