import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = 'a\nf'
    sys.stdin = io.StringIO(datastr)

    result = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert result == ['a', 'b', 'c', 'd', 'e', 'f']

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # print(regex_string)
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = 'f\na\na\nf'
    sys.stdin = io.StringIO(datastr)

    result = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert result == ['a', 'b', 'c', 'd', 'e', 'f']


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '1\n2\no\ns'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == ['o', 'p', 'q', 'r', 's']
