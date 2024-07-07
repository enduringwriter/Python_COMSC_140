import main
import random


def test_main_1():
    numbers = [5, 4, 3, 2, 1]

    print('Test data', numbers)
    main.bubble(numbers)
    print('After call bubble()', numbers)
    assert numbers == [4, 3, 2, 1, 5]


def test_main_2():
    numbers = [2, 3, 0, 5, 4]

    print('Test data', numbers)
    main.bubble(numbers)
    print('After call bubble()', numbers)
    assert numbers == [2, 0, 3, 4, 5]


def test_main_3():
    numbers = [random.randint(0, 10) for i in range(10)]
    print('Test data', numbers)
    main.bubble(numbers)
    print('After call bubble()', numbers)
    maxval = max(numbers)
    assert numbers[len(numbers) - 1] == maxval
# assert v1 == -10, "Min value does not match"
# assert v2 == 5, "Max value does not match"
