from p011_solution import *

def test_beginning():
    assert figunahe(25) == [1, 1, 2, 3, 5, 8, 13, 21]

def test_end():
    assert figunahe(70) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]