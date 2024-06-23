import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '40 \n 40 \n 20'
    sys.stdin = io.StringIO(datastr)

    m_perc, f_perc, nb_perc = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # res = re.search(r'[\w,\W]*100[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())
    m = f'{m_perc:.2f}'
    f = f'{f_perc:.2f}'
    nb = f'{nb_perc:.2f}'
    assert m == '40.00', 'Expect 40.00'
    assert f == '40.00', 'Expect 40.00'
    assert nb == '20.00', 'Expect 20.00'


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10 \n 20 \n 30'
    sys.stdin = io.StringIO(datastr)

    m_perc, f_perc, nb_perc = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # res = re.search(r'[\w,\W]*30[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())
    m = f'{m_perc:.2f}'
    f = f'{f_perc:.2f}'
    nb = f'{nb_perc:.2f}'
    assert m == '16.67', 'Expect 16.67'
    assert f == '33.33', 'Expect 33.33'
    assert nb == '50.00', 'Expect 50.00'
