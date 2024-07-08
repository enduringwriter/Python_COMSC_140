import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '30\n40\n'
    sys.stdin = io.StringIO(datastr)

    ret = main.getPrimeNumber(30, 40)
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    plist = list(ret)
    print(plist)
    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert len(plist) == 2
    assert isinstance(ret, types.GeneratorType) == True
    assert plist == [31, 37]


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '30\n50\n'
    sys.stdin = io.StringIO(datastr)

    ret = main.getPrimeNumber(30, 50)
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    plist = list(ret)
    print(plist)
    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert len(plist) == 5
    assert isinstance(ret, types.GeneratorType) == True
    assert plist == [31, 37, 41, 43, 47]
