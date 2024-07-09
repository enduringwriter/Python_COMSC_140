import main
import io
import sys
import re
import math


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '10 5 20 0 40 45 5\n40 10 5\n'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    numbers1 = [40, 10, 5]
    numbers2 = [10, 5, 20, 0, 40, 45, 50]
    ret = main.isSubList(numbers1, numbers2)
    print(f'Your return value is {ret}')
    assert ret == True, 'It should be True'


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '10 5 20 0 40 45 5\n40 10 5\n'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    numbers1 = [1, 2, 3, 4, 5, 6]
    numbers2 = [1, 2, 3]
    ret = main.isSubList(numbers1, numbers2)
    print(f'Your return value is {ret}')
    assert ret == False, 'It should be False'
