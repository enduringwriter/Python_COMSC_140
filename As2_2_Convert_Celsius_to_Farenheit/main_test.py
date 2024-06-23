import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '23'
    sys.stdin = io.StringIO(datastr)

    c, f = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # res = re.search(r'[\w,\W]*73\.40[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())
    cs = f'{c:.2f}'
    fs = f'{f:.2f}'
    assert cs == '23.00'
    assert fs == '73.40'


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '35'
    sys.stdin = io.StringIO(datastr)

    c, f = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    cs = f'{c:.2f}'
    fs = f'{f:.2f}'
    assert cs == '35.00'
    assert fs == '95.00'
    # res = re.search(r'[\w,\W]*95[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())
