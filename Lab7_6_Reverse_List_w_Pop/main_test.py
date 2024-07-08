import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 2 3 4 5'
    sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    numbers = main.getInput()
    print(f'The list values {numbers}')
    strlist = list(map(str, numbers))
    strval = ''.join(strlist[::-1])
    target = list(map(int, strval))
    print(f'Your result should be {target}')

    ret = main.makeReverse(numbers)

    print(f'Your return value is {ret}')
    assert ret == target


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '8 6 4 2 0'
    sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    numbers = main.getInput()
    print(f'The list values {numbers}')
    strlist = list(map(str, numbers))
    strval = ''.join(strlist[::-1])
    target = list(map(int, strval))
    print(f'Your result should be {target}')

    ret = main.makeReverse(numbers)

    print(f'Your return value is {ret}')
    assert ret == target


def test_main_3():
    detect = 0
    with open('main.py') as f:
        for line in f:
            if line.find('reverse(') != -1:
                detect = 1

    assert detect == 0, 'Do not use reverse() function'
