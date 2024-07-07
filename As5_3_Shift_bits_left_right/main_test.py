import random
import main


def test_shiftN1():

    str = '001100'
    print(int(str, 2))
    print('Test begins: shift left 2', 'test string : ', str)
    rstr = main.shiftN(str, 0, 2)
    print('Your result: ', rstr)
    print('Converted Decimal: ', int(rstr, 2))
    assert int(rstr, 2) == 48, "Expected 48"


def test_shiftN2():
    str = '110000'
    print(int(str, 2))
    rstr = main.shiftN(str, 1, 4)
    print('Test begins: shift right 4 ', 'test string : ', str)
    print('Your result: ', rstr)
    print('Converted Decimal: ', int(rstr, 2))

    assert int(rstr, 2) == 3, "Expected 3"
