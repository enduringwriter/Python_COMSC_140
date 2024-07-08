import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '35 5 10 20 40 15'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    number = [35, 5, 10, 20, 40, 15]
    main.bubble(number)
    print('After bubble() call', number)
    assert number == [5, 10, 20, 35, 15, 40]
    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    main.bubblesort(number)
    print('After bubblesort()) call', number)
    assert number == sorted(number)


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '3 2 1'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    number = [3, 2, 1]
    main.bubble(number)
    print('After bubble() call', number)
    assert number == [2, 1, 3]
    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    main.bubblesort(number)
    print('After bubblesort()) call', number)
    assert number == sorted(number)
