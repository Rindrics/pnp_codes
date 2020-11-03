from numdefs import baisu, baisu_3, baisu_5
import pytest


@pytest.mark.parametrize("multi, n, tail",
                         [(3, 1, 3), (3, 2, 6),
                          (5, 1, 5), (5, 2, 10),])
def test_baisu(multi, n, tail):
    assert baisu(multi=multi, n=n)[-1] == tail



def handler(func, **args):
    return func(**args)


testdata = {
    #   (multi, n, tail)
    'correct': [
        (3, 1, 3),
        (3, 2, 6),
        (3, 2, 6),
        (3, 3, 9),
        (3, 4, 18),
        (3, 5, 21),
        (3, 6, 24),
        (3, 7, 27),
        (3, 8, 33),
        (3, 9, 36),
        (3, 10, 39),
        (5, 1, 5),
        (5, 2, 10),
        (5, 3, 20),
        (5, 4, 25),
        (5, 5, 35),
        (5, 6, 40),
        (15, 1, 15),
    ],
    'wrong': [
        (3, 4, 12),
        (3, 4, 15),
        (3, 8, 30),
        (5, 3, 15),
        (5, 5, 30),
    ]
}


@pytest.mark.parametrize("multi, n, tail", testdata['correct'])
def test_baisu_tail(multi, n, tail):
    assert handler(baisu, multi=multi, n=n)[-1] == tail


@pytest.mark.parametrize("multi, n, tail", testdata['wrong'])
def test_baisu_tail_exceptions(multi, n, tail):
    assert not handler(baisu, multi=multi, n=n)[-1] == tail
