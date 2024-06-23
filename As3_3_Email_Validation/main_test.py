import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = 'john@company.com'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == True

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # res = re.search(r'[\w,\W]*[t,T]rue[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = 'john@company#com'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == False

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # res = re.search(r'[\w,\W]*[f,F]alse[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '2john@company.com'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert ret == False

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # res = re.search(r'[\w,\W]*[f,F]alse[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())


def test_main_4():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = 'johnbabartos@company.organization.gov'
    sys.stdin = io.StringIO(datastr)

    ret = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    assert ret == False

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # res = re.search(r'[\w,\W]*[f,F]alse[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())
