from src.calculator import sub

# shim so the autograder can find this test file name
from .test_subtraction import *  # noqa: F401,F403

def test_subtraction():
    assert sub(5, 3) == 2
    assert sub(0, 5) == -5
    assert sub(-1, -1) == 0


