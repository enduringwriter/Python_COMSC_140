import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '50'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == 'F'

    # res = re.search(r'[\w,\W]*F[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '65'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == 'D'


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '75'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == 'C'


def test_main_4():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '85'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == 'B'


def test_main_5():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '90'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == 'A'
