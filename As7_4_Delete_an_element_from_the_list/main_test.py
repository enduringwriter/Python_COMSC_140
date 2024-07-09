import main
import io
import sys
import re
import math


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '30\n'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    numbers = [5, 20, 30, 30, 35]
    print(f'Original list value: {numbers}')
    main.deleteOne(numbers, 30)
    print(f'After deleting 30 {numbers}')
    assert numbers == [5, 20, 35]


def test_main_2():
    numbers = [1, 1, 1, 1, 1]
    print(f'Original list value: {numbers}')
    main.deleteOne(numbers, 1)
    print(f'After deleting 1 {numbers}')
    assert numbers == []


def test_main_3():
    numbers = [1, 2, 3, 4, 5]
    print(f'Original list value: {numbers}')
    main.deleteOne(numbers, 6)
    print(f'After deleting 6 {numbers}')
    assert numbers == [1, 2, 3, 4, 5]
