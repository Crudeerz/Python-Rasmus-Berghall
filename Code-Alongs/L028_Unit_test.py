from L027_Module import square
import math




def test_positive_square():
    assert square(2) == 4
    assert square(5) == 25

def test_negative_square():
    assert square(-2) == 4
    assert square(-5) == 23

def test_zero_square():
    assert square(0) == 0




# print(L027_Module.square(9))
# print(L027_Module.sqrt(9))
# print(math.sqrt(9))
