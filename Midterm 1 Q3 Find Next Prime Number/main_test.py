import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = '15'
    sys.stdin = io.StringIO(datastr)

    pnumber = main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    assert pnumber == 17


def test_main_2():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = '20'
    sys.stdin = io.StringIO(datastr)

    pnumber = main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    assert pnumber == 23


def test_main_3():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = '10010'
    sys.stdin = io.StringIO(datastr)

    pnumber = main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    assert pnumber == 10037
