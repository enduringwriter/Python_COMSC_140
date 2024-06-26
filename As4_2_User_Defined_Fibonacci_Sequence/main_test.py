import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '1\n2\n5'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == [1, 2, 3, 5, 8], 'Should be 1, 2, 3, 5, 8'

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # regex_string = r'[\w,\W]*olleH'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '5\n8\n3'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == [5, 8, 13], 'Expected 5 8, 13'


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '5\n10\n5'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == [5, 10, 15, 25, 40], 'Expected 5 10 15 25 40'
