import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10'
    sys.stdin = io.StringIO(datastr)

    result = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert len(result) == 11
    target = []
    for i in range(len(result)):
        target.append(2**i)
    assert result == target

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # regex_string = r'[\w,\W]*1[\w,\W]*2[\w,\W]*4[\w,\W]*8[\w,\W]*16[\w,\W]*32[\w,\W]*64[\w,\W]*128[\w,\W]*256[\w,\W]*512[\w,\W]*1024[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '20'
    sys.stdin = io.StringIO(datastr)

    result = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert len(result) == 21
    target = []
    for i in range(len(result)):
        target.append(2**i)
    assert result == target


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '5'
    sys.stdin = io.StringIO(datastr)

    result = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert len(result) == 6
    target = []
    for i in range(len(result)):
        target.append(2**i)
    assert result == target
