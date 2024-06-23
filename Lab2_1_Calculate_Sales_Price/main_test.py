import main
import io
import sys
import re


def test_main_100_20():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '100 \n 20'
    sys.stdin = io.StringIO(datastr)

    original_price, discount_amount, final_price = main.main()
    sys.stdout = sys.__stdout__
    print('Captured\n', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    # p = re.compile('[\w,\W]*100[\w,\W]*')
    # res = p.match(lines[0])
    # print(res.group())
    # res = re.search('100', lines[0])
    # print(res.group())
    # assert res.group() == '100', 'Expected 100'
    assert original_price == 100, 'must be 100'
    assert discount_amount == 20, 'must be 20'
    assert final_price == 80, 'must be 80'


def test_main_200_40():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '200 \n 20'
    sys.stdin = io.StringIO(datastr)

    original_price, discount_amount, final_price = main.main()
    sys.stdout = sys.__stdout__
    print('Captured\n', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    # p = re.compile('[\w,\W]*100[\w,\W]*')
    # res = p.match(lines[0])
    # print(res.group())
    assert original_price == 200, 'must be 200'
    assert discount_amount == 40, 'must be 40'
    assert final_price == 160, 'must be 160'
