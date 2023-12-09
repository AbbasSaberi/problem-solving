from p017_solution import *

def test_beginning():
    assert P017(5) == ["00000",
                       "+0000",
                       "++000",
                       "+++00",
                       "++++0",
                       "+++++"]

def test_end():
    assert P017(3) == ["000",
                       "+00",
                       "++0",
                       "+++"]