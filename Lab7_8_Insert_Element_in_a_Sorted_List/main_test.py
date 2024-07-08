import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '10 15 25 30 35\n20'
    sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    numbers = main.getInput()
    print(f'The original list values: {numbers}')
    main.insertOne(numbers)
    print(f'After insertion 20: {numbers}')

    assert numbers == [10, 15, 20, 25, 30, 35]


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 2 3 4 5\n6'
    sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    numbers = main.getInput()
    print(f'The original list values: {numbers}')
    main.insertOne(numbers)
    print(f'After insertion 6: {numbers}')
    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert numbers == [1, 2, 3, 4, 5, 6]


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 2 3 4 5\n0'
    sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    numbers = main.getInput()
    print(f'The original list values: {numbers}')
    main.insertOne(numbers)
    print(f'After insertion 0: {numbers}')

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert numbers == [0, 1, 2, 3, 4, 5]


def test_main_4():
    detect = 0
    with open('main.py') as f:
        for line in f:
            if line.find('sort()') != -1:
                detect = 1
            if line.find('sorted') != -1:
                detect = 1
    assert detect == 0, 'Do not use any sort functions'
