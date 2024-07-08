
import main


def test_main_1():
    numbers = [2, 3, 0, 5, 4]

    first, others = main.splitlist(numbers)
    print(others)

    assert first == 0
    assert others == [3, 2, 5, 4]
# assert v1 == -10, "Min value does not match"
# assert v2 == 5, "Max value does not match"


def test_main_2():
    numbers = [5, 4, 3, 2, 1]

    first, others = main.splitlist(numbers)
    print(others)

    assert first == 1
    assert others == [4, 3, 2, 5]
# assert v1 == -10, "Min value does not match"
# assert v2 == 5, "Max value does not match"
