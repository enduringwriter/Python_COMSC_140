import random
import main


def test_main_1():
    numbers = [10, 20, 30, 15, 5]
    print('Original List', numbers)
    elst = [v for v in numbers if v % 2 == 0]
    target = min(elst)
    targetlen = len(numbers) - 1
    ret = main.mineven(numbers)
    print('Your function return this value: ', ret)
    print('After function call, Numbers: ', numbers)
    assert ret == target, 'Wrong return value '

    assert numbers == [20, 30, 15, 5], 'The list values are 20 30 15 5'


def test_main_2():
    numbers = [1, 3, 5, 7, 10, 14, 2, 8]
    print('Original List', numbers)
    elst = [v for v in numbers if v % 2 == 0]
    target = min(elst)
    targetlen = len(numbers) - 1
    ret = main.mineven(numbers)
    print('Your function return this value: ', ret)
    print('After function call, Numbers: ', numbers)
    assert ret == target, 'Wrong return value '

    assert numbers == [1, 3, 5, 7, 10, 14, 8], 'The list values are 20 30 15 5'


def test_main_3():
    N = random.randint(5, 20)
    numbers = [random.randint(-50, 50) for v in range(N)]
    print('Original List', numbers)
    elst = [v for v in numbers if v % 2 == 0]
    target = min(elst)
    targetlen = len(numbers) - 1
    ret = main.mineven(numbers)
    print('Your function return this value: ', ret)
    print('After function call, Numbers: ', numbers)
    assert ret == target, 'Wrong return value '

    assert targetlen == len(numbers), 'The length of list is not correct'
