from numdefs import baisu, candidate_meets_condition_of_baisu, others, baisu2
import pytest


@pytest.mark.parametrize('t_or_f, baisu, candidate',
                         [(True, 3, 3),
                          (True, 3, 6),
                          (True, 3, 9),
                          (False, 3, 12),
                          (True, 5, 5),
                          (True, 5, 10),
                          (False, 5, 15),
                          (True, 15, 15),
                          (True, 15, 30),
                          (True, 15, 45)])
def test_condition(t_or_f, baisu, candidate):
    assert candidate_meets_condition_of_baisu(baisu, candidate) == t_or_f


testdata = [
    (True, 3, 1, 3),
    (True, 3, 2, 6),
    (True, 3, 2, 6),
    (True, 3, 3, 9),
    (False, 3, 4, 12),
    (False, 3, 4, 15),
    (True, 3, 4, 18),
    (True, 3, 5, 21),
    (True, 3, 6, 24),
    (True, 3, 7, 27),
    (False, 3, 8, 30),
    (True, 3, 8, 33),
    (True, 3, 9, 36),
    (True, 3, 10, 39),
    (True, 5, 1, 5),
    (True, 5, 2, 10),
    (False, 5, 3, 15),
    (True, 5, 3, 20),
    (True, 5, 4, 25),
    (False, 5, 3, 30),
    (True, 5, 5, 35),
    (True, 5, 6, 40),
    (True, 15, 1, 15),
    (True, 15, 2, 30),
    (True, 15, 3, 45),
    (True, 15, 4, 60),
    (True, 15, 5, 75),
    (True, 15, 6, 90)
]


def handler(func, **args):
    return func(**args)


@pytest.mark.parametrize("t_or_f, multi, n, expect", testdata)
def test_baisu(t_or_f, multi, n, expect):
    assert (baisu(multi=multi, n=n) == expect) == t_or_f


def test_others():
    assert others(1) == 1
    assert others(2) == 2
    assert others(3) == 4
    assert others(4) == 7
    assert others(5) == 8
    assert others(6) == 11
    assert others(7) == 13
    assert others(8) == 14
    assert others(9) == 16
    assert others(10) == 17

@pytest.mark.parametrize("t_or_f, multi, n, expect", testdata)
def test_baisu2(t_or_f, multi, n, expect):
    assert (baisu2(multi=multi, n=n)[-1] == expect) == t_or_f
