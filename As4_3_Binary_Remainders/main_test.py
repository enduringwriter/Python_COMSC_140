import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '15'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    assert ret == [1, 1, 1, 1]

    # regex_string = r'[\w,\W]*1'
    # regex_string = r'[\w,\W]*1'
    # regex_string = r'[\w,\W]*1'
    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '7'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == [1, 1, 1]
    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '16'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    assert ret == [0, 0, 0, 0, 1]
    # regex_string = r'[\w,\W]*0'
    # regex_string += r'[\w,\W]*0'
    # regex_string += r'[\w,\W]*0'
    # regex_string += r'[\w,\W]*0'
    # regex_string += r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())
