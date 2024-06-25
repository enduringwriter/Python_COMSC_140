import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '5\n2\n3\n1\n5'
    sys.stdin = io.StringIO(datastr)

    ret, numbers = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == 16
    target = [5, 2, 3, 1, 5]
    assert len(numbers) == 5
    assert numbers == target

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # regex_string = r'[\w,\W]*16[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '1\n2\n3\n4\n5'
    sys.stdin = io.StringIO(datastr)

    ret, numbers = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == 15
    target = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
    assert numbers == target

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # regex_string = r'[\w,\W]*15[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10\n20\n30\n40\n50'
    sys.stdin = io.StringIO(datastr)

    ret, numbers = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    target = [10, 20, 30, 40, 50]
    assert ret == 150
    assert len(numbers) == 5
    assert numbers == target

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # regex_string = r'[\w,\W]*150[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())
