import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '25'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # res = re.search(r'[\w,\W]*less than 50[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())
    assert ret == 1, 'Range 1'


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '118'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # res = re.search(r'[\w,\W]*greater than 100[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())
    assert ret == 3, 'Range 3'


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

    # res = re.search(
    #     r'[\w,\W]*greater than 50[\w,\W]*less than 100[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())
    assert ret == 2, 'Range 2'
