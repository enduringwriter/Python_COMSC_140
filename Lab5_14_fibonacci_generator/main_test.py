import random
import main
import types


def test_main():

    N = 0
    gen = main.fibo(N)
    resultlst = list(gen)
    print('Your result: ', end=' ')
    for v in resultlst:
        print(v, end=' ')
    print()

    assert len(resultlst) == 1, "Wrong number of elements"
    assert resultlst[0] == 0, "Invalid value"

    N = 5
    gen = main.fibo(N)
    resultlst = list(gen)
    print('Your result: ', end=' ')
    for v in resultlst:
        print(v, end=' ')
    print()

    assert isinstance(gen, types.GeneratorType), 'Return value is not a generator'
    assert len(resultlst) == 6, "Wrong number of elements"
    assert resultlst == [0, 1, 1, 2, 3, 5]


def test_fibo2():

    N = 10
    gen = main.fibo(N)
    resultlst = list(gen)
    print('Your result: ', end=' ')
    for v in resultlst:
        print(v, end=' ')
    print()

    assert isinstance(gen, types.GeneratorType), 'Return value must be generator'
    assert len(resultlst) == 11, "Wrong number of elements"
    assert resultlst == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_yield():
    with open('main.py') as f:
        flag = False
        for line in f:
            if 'yield' in line:
                flag = True
                break

    assert flag == True
