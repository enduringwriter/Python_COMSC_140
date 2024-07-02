import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = '10\n20\n'
    sys.stdin = io.StringIO(datastr)

    # main.main()
    num1, num2 = main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    assert num1 == 0
    assert num2 == 0
    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())
