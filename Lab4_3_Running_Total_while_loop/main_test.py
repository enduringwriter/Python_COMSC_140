import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '5\n2\n3\n1\n5'
    sys.stdin = io.StringIO(datastr)

    retval = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # regex_string = r'[\w,\W]*16[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())
    assert retval == 16


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '1\n2\n3\n4\n5'
    sys.stdin = io.StringIO(datastr)

    retval = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # regex_string = r'[\w,\W]*15[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())
    assert retval == 15


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10\n20\n30\n40\n50'
    sys.stdin = io.StringIO(datastr)

    retval = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # regex_string = r'[\w,\W]*150[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())
    assert retval == 150
