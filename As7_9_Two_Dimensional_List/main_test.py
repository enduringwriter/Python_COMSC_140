import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    # datastr = 'are arrow amore aspire aero'
    # sys.stdin = io.StringIO(datastr)

    # rsum, csum, rowidx, maxnum = main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    numbers = [[99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24, 56],
               [33, 77, 32, 33, 34]]
    ret = main.getMaxElement(numbers)
    print('Return value from getMaxElement', ret)
    assert ret == 99

    ret = main.getSumRows(numbers)
    print('Return value from getSumRows', ret)
    assert ret == [317, 298, 209]

    ret = main.getSumCols(numbers)
    print('Return value from getSumCols', ret)
    assert ret == [176, 109, 163, 207, 113, 56]

    ret = main.getMaxElmRow(numbers)
    print('Return value from getMaxElmRow', ret)
    assert ret == [99, 88, 77]

    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())
