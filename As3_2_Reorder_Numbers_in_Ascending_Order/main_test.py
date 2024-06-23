import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10\n2\n1\n'
    sys.stdin = io.StringIO(datastr)

    minval, median, maxval = main.main()

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert minval == 1
    assert median == 2
    assert maxval == 10
    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # res = re.search(r'[\w,\W]*1[\w,\W]*2[\w,\W]*10[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '2\n3\n1\n'
    sys.stdin = io.StringIO(datastr)

    minval, median, maxval = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert minval == 1
    assert median == 2
    assert maxval == 3
    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # res = re.search(r'[\w,\W]*1[\w,\W]*2[\w,\W]*3[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '2\n1\n3\n'
    sys.stdin = io.StringIO(datastr)

    minval, median, maxval = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert minval == 1
    assert median == 2
    assert maxval == 3
    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # res = re.search(r'[\w,\W]*1[\w,\W]*2[\w,\W]*3[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())
