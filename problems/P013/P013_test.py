from p013_solution import *

def test_beginning():
    assert P013(4) == [2 , 2]

def test1():
    assert P013(42) == [2 , 3 , 7]

def test2():
    assert P013(88) == [2 , 2 , 2 , 11]

def test_end():
    assert P013(39) == [3 , 13]