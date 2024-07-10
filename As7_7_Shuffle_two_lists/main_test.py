import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    # datastr = '1 2 3\n4 5 6 7'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())
    num1 = [1, 2, 3]
    num2 = [4, 5, 6, 7]
    ret = main.shuffle(num1, num2)
    print(f'The return value is: {ret}')
    assert ret == [1, 4, 2, 5, 3, 6, 7]


def test_main_2():
    captureout = io.StringIO()
    sys.stdout = captureout
    # datastr = '1 2 3 4 5\n6 7 8'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())
    num1 = [1, 2, 3, 4, 5]
    num2 = [6, 7, 8]
    ret = main.shuffle(num1, num2)
    print(f'The return value is: {ret}')
    assert ret == [1, 6, 2, 7, 3, 8, 4, 5]
