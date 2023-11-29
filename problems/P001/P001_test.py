from P001 import *

def test1():
    assert even_odd(38) == '38 is even'

def test2():
    assert even_odd(45) == '45 is odd'

def test3():
    assert even_odd(14) == '14 is even'

def test4():
    assert even_odd(3) == '3 is odd'

def test5():
    assert even_odd(210) == '210 is even'

def test6():
    assert even_odd(59) == '59 is odd'

def test7():
    assert even_odd(66) == '66 is even'

def test8():
    assert even_odd(81) == '81 is odd'

def test9():
    assert even_odd(2) == '2 is even'

def test10():
    assert even_odd(875) == '875 is odd'

def test_end():
    assert even_odd(93460289035709328590232945795479417954716754974157985985298) == '93460289035709328590232945795479417954716754974157985985298 is even'