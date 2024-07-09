import main
import io
import sys
import re


sumtwo = lambda x: x[0] + x[1]


def test_main_0():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 2 3\n 4 5 6\n'
    sys.stdin = io.StringIO(datastr)

    list1 = main.getInput()
    list2 = main.getInput()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    print(f'The inpust list 1: \t{list1}')
    print(f'The inpust list 2: \t{list2}')

    ret = main.listSum(list1, list2)
    print(f'Your retrun value is:\t {ret}')
    target = list(map(sumtwo, tuple(zip(list1, list2))))
    print(f'The result must be \t{target}')
    assert ret == target


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 3 4 5 2 7 8 1 2 5\n 7 8 1 2 5 1 3 5 4 2\n'
    sys.stdin = io.StringIO(datastr)

    list1 = main.getInput()
    list2 = main.getInput()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    print(f'The inpust list 1:\t {list1}')
    print(f'The inpust list 2:\t {list2}')

    ret = main.listSum(list1, list2)
    print(f'Your retrun value is:\t {ret}')
    target = list(map(sumtwo, tuple(zip(list1, list2))))
    print(f'The result must be \t{target}')
    assert ret == target
