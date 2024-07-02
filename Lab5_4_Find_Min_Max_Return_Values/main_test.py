
import main
import random


def test_main_1():

    numbers = [-10, 20, 30, 40, -50]
    minval, maxval = main.minmax(numbers)

    assert maxval == 40, "Max value does not match"
    assert minval == -50, "Min value does not match"


def test_main_2():

    numbers = [random.randint(0, 100) for i in range(10)]
    miv = min(numbers)
    mav = max(numbers)
    minval, maxval = main.minmax(numbers)

    assert maxval == mav, "Min value does not match"
    assert minval == miv, "Max value does not match"
