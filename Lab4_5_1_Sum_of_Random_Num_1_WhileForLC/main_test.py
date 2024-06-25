import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'A\nB\n30'
    # sys.stdin = io.StringIO(datastr)

    numbers, total = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    # rdvals = list(map(int, lines[0].split()))
    # print(rdvals)
    print(lines)

    target = sum(numbers)
    assert target == total

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # tot = sum(rdvals)
    # print('total ', tot)
    # regex_string = r'[\w,\W]*' + str(tot) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[1])
    # assert res != None
    # print(res.group())
