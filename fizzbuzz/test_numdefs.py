from numdefs import baisu_3, baisu_5
import pytest


testdata_for_3 = [
    (1, 3),
    (2, 6),
    (2, 6),
    (3, 9),
    (4, 18),
    (5, 21),
    (6, 24),
    (7, 27),
    (8, 33),
    (9, 36),
    (10, 39)
]

@pytest.mark.parametrize("n, lastone", testdata_for_3)
def test_baisu_3(n, lastone):
    assert baisu_3(n=n)[-1] == lastone

def test_baisu_3_exceptions():
    assert baisu_3(n=4)[-1] != 12 and\
           baisu_3(n=4)[-1] != 15 and\
           baisu_3(n=8)[-1] != 30

def test_baisu_5():
    assert baisu_5(n=1) == [5] and\
           baisu_5(n=2) == [5, 10] and\
           baisu_5(n=3) == [5, 10, 20] and\
           baisu_5(n=4) == [5, 10, 20, 25] and\
           baisu_5(n=5) == [5, 10, 20, 25, 35]

def test_baisu_5_exceptions():
    assert baisu_5(n=3)[-1] != 15 and\
           baisu_5(n=5)[-1] != 30
# def test_consecutive():
#     assert consecutive(n=1) == [12]
#     assert consecutive(n=2) == [12, 34]

# def test_others():
#     assert others(n=1) == [1]
#     assert others(n=2) == [1, 2]
#     assert others(n=3) == [1, 2, 4]
#     assert others(n=4) == [1, 2, 4, 7]
#     assert others(n=5) == [1, 2, 4, 7, 8]
#     assert others(n=6) == [1, 2, 4, 7, 8, 11]
#     assert others(n=7) == [1, 2, 4, 7, 8, 11, 13]
#     assert others(n=8) == [1, 2, 4, 7, 8, 11, 13, 14]
#     assert others(n=9) == [1, 2, 4, 7, 8, 11, 13, 14, 16]
