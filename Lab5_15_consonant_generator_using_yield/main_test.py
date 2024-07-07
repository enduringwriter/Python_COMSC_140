import random
import main
import types


def test_main():

    strval = 'Python Programming'
    mygen = main.consonant(strval)
    resultlst = list(mygen)
    print('Your result: ', end=' ')
    for v in resultlst:
        print(v, end=' ')
    print()

    assert isinstance(mygen, types.GeneratorType)
    print(resultlst)
    assert len(resultlst) == 13, "Wrong number of elements"
    assert resultlst == ['P', 'y', 't', 'h', 'n', 'P', 'r', 'g', 'r', 'm', 'm', 'n', 'g']


def test_fibo2():

    strval = 'PAYETIHONU'
    mygen = main.consonant(strval)
    resultlst = list(mygen)
    print('Your result: ', end=' ')
    for v in resultlst:
        print(v, end=' ')
    print()

    assert isinstance(mygen, types.GeneratorType)
    assert len(resultlst) == 5, "Wrong number of elements"
    print(resultlst)
    assert resultlst == ['P', 'Y', 'T', 'H', 'N']


def test_yield():
    with open('main.py') as f:
        flag = False
        for line in f:
            if 'yield' in line:
                flag = True
                break

    assert flag == True
