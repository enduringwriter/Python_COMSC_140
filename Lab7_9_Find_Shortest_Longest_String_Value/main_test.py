import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    # datastr = 'James Robert Kurt Bill Matt'
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

    names = ['Albert', 'Joanne', 'Kurt', 'Bill', 'Matt']
    longest, shortest = main.findNames(names)
    print(f'Your result: Longest: {longest}, Shortest: {shortest}')
    assert shortest == 'Bill'
    assert longest == 'Joanne'


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    # datastr = 'AAA Z A BBB aaaaa'
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
    names = ['AAA', 'Z', 'A', 'BBB', 'aaaaa']
    longest, shortest = main.findNames(names)
    print(f'Your result: Longest: {longest}, Shortest: {shortest}')
    assert shortest == 'A'
    assert longest == 'aaaaa'
