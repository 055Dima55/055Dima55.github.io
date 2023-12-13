from HW_9 import add_three_numbers
import pytest

def test_1():
    assert add_three_numbers(3, 2, 10) == 15
def test_2():
    assert add_three_numbers(1, 1, 10) == 12


@pytest.mark.parametrize("num_1, num_2, num_3, result", [
    pytest.param(3, 2, 10, 15, id="first" ),
    pytest.param(1, 1, 2, 4, id="sekond" )])

def test_mark_1(num_1, num_2, num_3, result):
    assert add_three_numbers(num_1, num_2, num_3) == result



list_test_3 = [(3, 2, 10, 15), (1, 1, 2, 4,)]
@pytest.mark.parametrize("num_1, num_2, num_3, result", list_test_3)
def test_mark_1(num_1, num_2, num_3, result):
    assert add_three_numbers(num_1, num_2, num_3) == result