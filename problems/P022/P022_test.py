from p022_solution import *

def test1():
    a = 4

    b = ['2' , '5' , '13' , '1']

    B = ['7' , '82' , '20' , '6']

    assert P022(a , b , B) == '9 87 33 7'

def test2():
    a = 6

    b = ['3' , '21' , '3' , '7' , '5' , '19']

    B = ['2' , '2' , '14' , '567' , '91' , '8']

    assert P022(a , b , B) == '5 23 17 574 96 27'