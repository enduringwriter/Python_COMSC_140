import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10\n97\n45\n'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == 97


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '100\n50\n10'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == 100


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '1\n2\n3\n'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == 3
