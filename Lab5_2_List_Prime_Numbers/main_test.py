import random
import main


def test_primeNumbers1():

    begin = 0
    end = 20
    print('Test begins: begin = ', begin, ' end: ', end)
    rlst = main.primeNumbers(begin, end)

    print('Your list: ', rlst)

    assert len(rlst) == 8, "Invalid value. Expected 8"
    assert rlst[0] == 2, "Expected 2"
    assert rlst[1] == 3, "Expected 3"
    assert rlst[2] == 5, "Expected 5"
    assert rlst[3] == 7, "Expected 7"
    assert rlst[4] == 11, "Expected 11"
    assert rlst[5] == 13, "Expected 13"
    assert rlst[6] == 17, "Expected 17"
    assert rlst[7] == 19, "Expected 19"


def test_primeNumbers2():
    begin = 10
    end = 50
    print('Test begins: begin = ', begin, ' end: ', end)
    rlst = main.primeNumbers(begin, end)

    print('Your list: ', rlst)

    assert len(rlst) == 11, "Invalid value. Expected 11"
    assert rlst[0] == 11, "Expected 11"
    assert rlst[1] == 13, "Expected 13"
    assert rlst[2] == 17, "Expected 17"
    assert rlst[3] == 19, "Expected 19"
    assert rlst[4] == 23, "Expected 23"
    assert rlst[5] == 29, "Expected 29"
    assert rlst[6] == 31, "Expected 31"
    assert rlst[7] == 37, "Expected 37"
    assert rlst[8] == 41, "Expected 41"
    assert rlst[9] == 43, "Expected 43"
    assert rlst[10] == 47, "Expected 47"
