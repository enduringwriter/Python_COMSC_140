import main
import io
import sys
import re


def test_main_1():
    # captureOut = io.StringIO()
    # sys.stdout = captureOut
    # # datastr = '10\n25\n15\n35\n50'
    # # sys.stdin = io.StringIO(datastr)

    # sys.stdout = sys.__stdout__
    # print('Captured ', captureOut.getvalue())
    # lines = captureOut.getvalue().split('\n')
    # print(lines)

    # regex_string = r'[\w,\W]*75'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())
    numbers = [10, 25, 15, 35, 50]
    ret = main.getSum(numbers)
    print(f'The return value is {ret}')
    assert ret == 75


def test_main_2():
    numbers = [3, 8, 2, 6, 1, 9, 4, 7]
    ret = main.getSum(numbers)
    print(f'The return value is {ret}')
    assert ret == 30
