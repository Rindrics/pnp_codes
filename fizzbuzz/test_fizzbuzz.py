import pytest
from fizzbuzz import generate_fizzbuzz_msg
from numdefs import baisu, others


n_tests = 10
test_seq = range(1, n_tests + 1)


def generate_baisu_seq(multi):
    return map(baisu, [multi] * len(test_seq), test_seq)

@pytest.mark.parametrize('fizz_numbers',
                         generate_baisu_seq(3))
def test_return_fizz(fizz_numbers):
    assert generate_fizzbuzz_msg(fizz_numbers) == 'Fizz'


@pytest.mark.parametrize('buzz_numbers',
                         generate_baisu_seq(5))
def test_return_buzz(buzz_numbers):
    assert generate_fizzbuzz_msg(buzz_numbers) == 'Buzz'


@pytest.mark.parametrize('fizzbuzz_numbers',
                         generate_baisu_seq(15))
def test_return_fizzbuzz(fizzbuzz_numbers):
    assert generate_fizzbuzz_msg(fizzbuzz_numbers) == 'FizzBuzz'


@pytest.mark.parametrize('others', map(others, test_seq))
def test_return_asis(others):
    assert generate_fizzbuzz_msg(others) == str(others)


@pytest.mark.parametrize('consecutive', [12, 34])
def test_return_renban(consecutive):
    assert generate_fizzbuzz_msg(consecutive) == str(consecutive) + '連番!'
