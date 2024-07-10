import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    # datastr = '1 2 3\n4 5 6 7 8'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    num1 = [1, 3, 5, 7]
    num2 = [2, 4, 6, 8]
    merged = main.mergeList(num1, num2)
    print(f'The merged list is {merged}')
    assert merged == [1, 2, 3, 4, 5, 6, 7, 8]


def test_main_2():
    num1 = [1, 2, 3, 4]
    num2 = [5, 6, 7, 8]
    merged = main.mergeList(num1, num2)
    print(f'The merged list is {merged}')
    assert merged == [1, 2, 3, 4, 5, 6, 7, 8]


def test_main_3():
    num1 = [5, 10, 25, 75, 85]
    num2 = [45, 55, 60]
    merged = main.mergeList(num1, num2)
    print(f'The merged list is {merged}')
    assert merged == [5, 10, 25, 45, 55, 60, 75, 85]
