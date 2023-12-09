from p031_solution import *

def test_1():
    assert P031(10) == [(3, 7),
                        (5, 5),
                        (7, 3)]

def test_2():
    assert P031(26) == [(3, 23),
                        (7, 19),
                        (13, 13),
                        (19, 7),
                        (23, 3)]

def test_3():
    assert P031(75) == ["75 is odd"]

def test_4():
    assert P031(52) == [(5, 47),
                        (11, 41),
                        (23, 29),
                        (29, 23),
                        (41, 11),
                        (47, 5)]