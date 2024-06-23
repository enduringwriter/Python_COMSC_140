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

    assert ret == 1, 'The result should be 1'
    # res = re.search('[\w,\W]*odd[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())


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

    assert ret == 0, 'The result should be 0'
    # res = re.search('[\w,\W]*even[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())
