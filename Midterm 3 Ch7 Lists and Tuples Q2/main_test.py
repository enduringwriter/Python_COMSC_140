import main
import random


def test_main_1():
    numbers = [3, 8, 9, 6, 5]
    ret = main.getSum(numbers, 3)
    print(f'Your return value: {ret}')
    assert ret == 23


def test_main_2():
    numbers = [1, 2, 3, 4, 5]
    ret = main.getSum(numbers, 3)
    print(f'Your return value: {ret}')
    assert ret == 12


def test_main_3():
    numbers = [5, 4, 3, 2, 1]
    ret = main.getSum(numbers, 5)
    print(f'Your return value: {ret}')
    assert ret == 15


def test_main_4():
    numbers = [5, 4, 3, 2, 1]
    ret = main.getSum(numbers, 1)
    print(f'Your return value: {ret}')
    assert ret == 5


def test_main_5():
    numbers = [19, 5, -40, 44, 23, 33, -30, 33, -50, -25]
    ret = main.getSum(numbers, 5)
    print(f'Your return value: {ret}')
    assert ret == 103


def test_main_6():
    numbers = [-2, -3, -47, 50, -40, -29, -38, 16, -13, -35]
    ret = main.getSum(numbers, 5)
    print(f'Your return value: {ret}')
    assert ret == -41
