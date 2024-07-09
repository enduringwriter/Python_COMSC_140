import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '1 2 3 4 5\n2'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    numbers = [25, 15, 5, 10, 0]
    main.findSmallest(numbers, 0)
    print(f'Find the 1st smallest number: {numbers}')
    assert numbers[0] == 0
    main.findSmallest(numbers, 1)
    print(f'Find the 2nd smallest number: {numbers}')
    assert numbers[1] == 5
    main.findSmallest(numbers, 2)
    print(f'Find the 3rd smallest number: {numbers}')
    assert numbers[2] == 10
    main.findSmallest(numbers, 3)
    print(f'Find the 4th smallest number: {numbers}')
    assert numbers[3] == 15
    main.findSmallest(numbers, 4)
    print(f'Find the 5th smallest number: {numbers}')
    assert numbers[4] == 25
    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '5 25 15 10 0\n3'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    numbers = [25, 15, 5, 10, 0]
    main.selectionSort(numbers)
    print(f'After call selectionSort(): {numbers}')
    assert numbers == [0, 5, 10, 15, 25]
    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
