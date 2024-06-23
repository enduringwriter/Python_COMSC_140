import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '10 \n 20 \n 30'
    # sys.stdin = io.StringIO(datastr)

    sub1, sub2, merged_str = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # res = re.search(r'[\w,\W]*Programming[\w,\W]*', lines[0])

    assert sub1 == 'Python'
    assert sub2 == 'Programming'
    assert merged_str == 'Programming Python'
