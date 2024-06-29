import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = 'program\npyton\njava\nc++\nstop'
    sys.stdin = io.StringIO(datastr)

    longest, shortest = main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    assert longest == 'program'
    assert shortest == 'c++'

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
    datastr = 'abc\nbbb\nxxx\nzz\nphp\nstop'
    sys.stdin = io.StringIO(datastr)

    longest, shortest = main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    assert longest == 'abc'
    assert shortest == 'zz'

    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())
