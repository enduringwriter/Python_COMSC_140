import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    # datastr = '1 3 2\n1 2 3 4 5'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    num1 = [20, 30, 35]
    num2 = [5, 20, 30, 35, 50]
    ret = main.isSubset(num1, num2)
    print(f'Your return value is {ret}')  # True
    assert ret == True


def test_main_2():
    num1 = [1, 3, 2]
    num2 = [1, 2, 3, 4, 5]
    ret = main.isSubset(num1, num2)
    print(f'Your return value is {ret}')  # True
    assert ret == False


def test_main_3():
    num1 = [1, 4, 5]
    num2 = [1, 2, 3, 4, 5]
    ret = main.isSubset(num1, num2)
    print(f'Your return value is {ret}')  # True
    assert ret == False


def test_main_4():
    num1 = [1, 3, 2]
    num2 = [4, 1, 3, 2, 5]
    ret = main.isSubset(num1, num2)
    print(f'Your return value is {ret}')  # True
    assert ret == True
