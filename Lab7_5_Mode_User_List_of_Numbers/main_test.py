import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 2 2 4 2\n'
    sys.stdin = io.StringIO(datastr)

    numbers = main.getInput()
    ret = main.findMost(numbers)
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    print(f'The list values {numbers}')
    print(f'Your return value is {ret}')

    assert ret == 2


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 1 1 1 2 2 2 3 3 3 3 3\n'
    sys.stdin = io.StringIO(datastr)

    numbers = main.getInput()
    ret = main.findMost(numbers)
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    print(f'The list values {numbers}')
    print(f'Your return value is {ret}')

    assert ret == 3
