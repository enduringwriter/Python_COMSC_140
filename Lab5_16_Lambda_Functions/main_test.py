import random
import main


def test_greater():

    assert main.greater(10, 20) == 20, "Invalid greater value"
    assert main.greater(20, 10) == 20, "Invalid greater value"
    assert main.greater(100, 20) == 100, "Invalid greater value"


def test_filter50():

    numbers = [random.randint(0, 100) for i in range(10)]
    print('original list', numbers)
    tlst = [v for v in numbers if v > 50]
    tnum = len(tlst)
    rlst = main.filter50(numbers)
    print('filter 50', rlst)

    assert len(rlst) == len(tlst), "Wrong number of elements"
    flag = 1
    for v in tlst:
        if v not in rlst:
            flag = 0
    assert flag == 1, 'The list values are wrong'

    # flag = 0
    # for i in range(len(rlst)):
    #     if rlst[i] == tlst[i]:
    #         flag = 1
    # assert flag == 1, "Invalid elements for > 50"


def test_yield():
    with open('main.py') as f:
        flag = False
        for line in f:
            if 'lambda' in line:
                flag = True
                break

    assert flag == True
