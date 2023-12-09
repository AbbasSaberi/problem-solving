from p009_solution import *

def test_beginning():
    assert is_preme(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_end():
    assert is_preme(54) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]