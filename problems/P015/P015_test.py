from p015_solution import *

def test1():
    a = 5

    b = [4 , 8 , 6 , 2 , 10]

    assert P015(a , b) == 30

def test2():
    a = 3

    b = [8 , 2 , 8]

    assert P015(a , b) == 18