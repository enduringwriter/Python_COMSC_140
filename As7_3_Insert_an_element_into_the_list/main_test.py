import main
import io
import sys
import re
import math


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '25\n'
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

    numbers = [5, 20, 30, 35, 50]
    print(f'The original value {numbers}')
    main.insertOne(numbers, 25)
    print(f'After insertion 25 {numbers}')
    assert numbers == [5, 20, 25, 30, 35, 50]


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '0\n'
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
    numbers = [1, 2, 3, 4, 5]
    print(f'The original value {numbers}')
    main.insertOne(numbers, 0)
    print(f'After insertion 0 {numbers}')
    assert numbers == [0, 1, 2, 3, 4, 5]


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '0\n'
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
    numbers = [1, 2, 3, 4, 5]
    print(f'The original value: {numbers}')
    main.insertOne(numbers, 6)
    print(f'After insertion 6 {numbers}')

    assert numbers == [1, 2, 3, 4, 5, 6]


def test_main_4():
    result = False
    with open('main.py') as f:
        for line in f:
            if 'sort(' in line:
                result = True
            if 'sorted(' in line:
                result = True
    assert result == False
