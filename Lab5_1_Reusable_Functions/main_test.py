import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = '10\n20\n'
    sys.stdin = io.StringIO(datastr)

    # main.main()
    n1 = main.getinput()
    n2 = main.getinput()
    ret = main.getsum(n1, n2)
    main.printval(n1, n2, ret)
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())

    assert n1 == 10
    assert n2 == 20
    assert ret == 30
