from numdefs import baisu_3, baisu_5#, baisu_15, consecutive, others


def test_baisu_3():
    assert baisu_3(n=1) == [3] and\
           baisu_3(n=2) == [3, 6] and\
           baisu_3(n=3) == [3, 6, 9] and\
           baisu_3(n=4) == [3, 6, 9, 18] and\
           baisu_3(n=5) == [3, 6, 9, 18, 21] and\
           baisu_3(n=6) == [3, 6, 9, 18, 21, 24] and\
           baisu_3(n=7) == [3, 6, 9, 18, 21, 24, 27] and\
           baisu_3(n=8) == [3, 6, 9, 18, 21, 24, 27, 33] and\
           baisu_3(n=9) == [3, 6, 9, 18, 21, 24, 27, 33, 36] and\
           baisu_3(n=10) == [3, 6, 9, 18, 21, 24, 27, 33, 36, 39]

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
