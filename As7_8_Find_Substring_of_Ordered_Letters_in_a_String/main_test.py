import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    # datastr = 'are arrow amore aspire aero'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    words = ['are', 'arrow', 'amore', 'aspire', 'assertive', 'arrogant', 'bartender', 'carter']
    are = ['a', 'r', 'e']
    ret = main.hasARE(words)
    print(f'The result is: {ret}')
    print(f"Expected Result: ['are', 'amore', 'aspire', 'assertive', 'bartender', 'carter'] ")
    assert ret == ['are', 'amore', 'aspire', 'assertive', 'bartender', 'carter']


def test_main_2():
    words = ['assertive', 'arrogant', 'bartender', 'carter', 'racer']
    are = ['a', 'r', 'e']
    ret = main.hasARE(words)
    print(f'The result is: {ret}')
    print(f"Expected Result: ['assertive', 'bartender', 'carter']")
    assert ret == ['assertive', 'bartender', 'carter']
