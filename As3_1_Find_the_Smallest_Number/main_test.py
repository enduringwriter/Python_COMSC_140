import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '10\n2\n2\n'
    # sys.stdin = io.StringIO(datastr)

    n1, n2, n3, mv = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    minval = min(n1, n2, n3)
    assert mv == minval
    # rvalues = list(map(int, lines[0].split()))
    # print(rvalues)
    # minval = min(rvalues)

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[1])
    # assert res != None
    # print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '10\n2\n2\n'
    # sys.stdin = io.StringIO(datastr)

    n1, n2, n3, mv = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    minval = min(n1, n2, n3)
    assert mv == minval
    # rvalues = list(map(int, lines[0].split()))
    # print(rvalues)
    # minval = min(rvalues)

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[1])
    # assert res != None
