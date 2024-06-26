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
    print(lines)

    gt100 = [v for v in numbers if v > 100]
    assert gt100 == [], 'Random values should be >0 and <100'
    assert total == sum(numbers[:-1]), 'Total is not valid'
    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # regex_string = r'[\w,\W]*' + str(tot) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[1])
    # assert res != None
    # print(res.group())
