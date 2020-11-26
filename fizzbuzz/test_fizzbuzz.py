import pytest
from fizzbuzz import generate_call
from numdefs import baisu, others, baisu2


n_tests = 10
test_seq = range(1, n_tests + 1)


def generate_baisu_seq(multi):
    return map(baisu, [multi] * len(test_seq), test_seq)


@pytest.mark.parametrize('fizz_number',
                         generate_baisu_seq(3))
def test_return_fizz(fizz_number):
    assert generate_call(fizz_number) == 'Fizz'


@pytest.mark.parametrize('buzz_number',
                         generate_baisu_seq(5))
def test_return_buzz(buzz_number):
    assert generate_call(buzz_number) == 'Buzz'


@pytest.mark.parametrize('fizzbuzz_number',
                         generate_baisu_seq(15))
def test_return_fizzbuzz(fizzbuzz_number):
    assert generate_call(fizzbuzz_number) == 'FizzBuzz'


@pytest.mark.parametrize('others', map(others, test_seq))
def test_return_asis(others):
    assert generate_call(others) == str(others)


@pytest.mark.parametrize('consecutive', [12, 34])
def test_return_renban(consecutive):
    assert generate_call(consecutive) == str(consecutive) + '連番!'


n_tests = 100
baisu3 = baisu2(multi=3, n=n_tests)
baisu5 = baisu2(multi=5, n=n_tests)
baisu15 = baisu2(multi=15, n=n_tests)
@pytest.mark.parametrize('fizz_number', baisu3)
def test_return_fizz2(fizz_number):
    assert generate_call(fizz_number) == 'Fizz'

@pytest.mark.parametrize('fizz_number', baisu5)
def test_return_buzz2(fizz_number):
    assert generate_call(fizz_number) == 'Buzz'

@pytest.mark.parametrize('fizz_number', baisu15)
def test_return_buzz2(fizz_number):
    assert generate_call(fizz_number) == 'FizzBuzz'
