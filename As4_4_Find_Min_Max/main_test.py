import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10\n45\n50\n35\n25'
    sys.stdin = io.StringIO(datastr)

    numbers, maxval, minval = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert numbers == [10, 45, 50, 35, 25]
    assert maxval == 50
    assert minval == 10


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '-10\n33\n55\n20\n-5'
    sys.stdin = io.StringIO(datastr)

    numbers, maxval, minval = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert numbers == [-10, 33, 55, 20, -5], 'list values are not valid'
    assert maxval == 55, 'max 55'
    assert minval == -10, 'min -10'
