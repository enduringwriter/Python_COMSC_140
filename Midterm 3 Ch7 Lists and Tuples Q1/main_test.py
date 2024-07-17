import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    # datastr = 'Python\n3 4 1 2 0 5'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    strval = 'Python'
    indices = [1, 2, 3, 4, 5, 0]
    ret = main.encrypt(strval, indices)
    print(f'Your return value: {ret}')
    assert isinstance(ret, str) == True
    assert ret == 'nPytho'
    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())


def test_main_2():
    captureout = io.StringIO()
    sys.stdout = captureout
    # datastr = 'Python\n0 5 1 2 3 4'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    strval = 'Python'
    indices = [3, 4, 1, 2, 5, 0]
    ret = main.encrypt(strval, indices)
    print(f'Your return value: {ret}')
    assert isinstance(ret, str) == True
    assert ret == 'nthPyo'
    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())


def test_main_3():
    captureout = io.StringIO()
    sys.stdout = captureout
    # datastr = 'Python\n0 5 1 2 3 4'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    strval = 'Python'
    indices = [0, 5, 1, 2, 3, 4]
    ret = main.encrypt(strval, indices)
    print(f'Your return value: {ret}')
    assert isinstance(ret, str) == True
    assert ret == 'Pthony'
    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())
