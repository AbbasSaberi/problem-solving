from p014_solution import *

def test1():
    a = 2

    b = ["Ali" , "Hassan"]

    A = 3

    B = ["Reza" , "Milad" , "Mohsen"]

    assert P014(a , b , A , B) == ['Ali', 'Hassan', 'Reza', 'Milad', 'Mohsen']

def test2():
    a = 2

    b = ["Hossein" , "Abbas"]

    A = 2

    B = ["Fateme" , "Ali"]

    assert P014(a , b , A , B) == ['Hossein', 'Abbas', 'Fateme', 'Ali']