import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10 \n 20 \n 30'
    sys.stdin = io.StringIO(datastr)

    total, average = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # p = re.compile(r'[\w,\W]*10[\w,\W]*20[\w,\W]*30[\w,\W]*')
    # res = p.match(lines[0])
    # print(res.group())
    assert total == 60
    assert int(average) == 20


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10 \n 15 \n 25'
    sys.stdin = io.StringIO(datastr)

    total, average = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # p = re.compile(r'[\w,\W]*10[\w,\W]*15[\w,\W]*25[\w,\W]*')
    # res = p.match(lines[0])
    # print(res.group())
    assert total == 50
    assert int(average) == 16
