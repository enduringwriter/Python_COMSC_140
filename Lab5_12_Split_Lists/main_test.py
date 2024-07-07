import random
import main


def test_main_1():
    numbers = [3, 2, 0, 5, 4]
    # print (id(numbers))
    print('Test data', numbers)
    numbers = main.split(numbers)
    print('After split() ', numbers)
    # print (id(numbers))
    assert numbers[2] == 3
    assert numbers[0] <= 3
    assert numbers[1] <= 3
    assert numbers[3] > 3
    assert numbers[4] > 3


def test_main_2():
    numbers = [random.randint(0, 20) for i in range(10)]
    print('Test data', numbers)
    pivot = numbers[0]
    cnt = numbers.count(pivot)

    numbers = main.split(numbers)

    start = 0
    for i in range(cnt):
        try:
            pivotidx = numbers.index(pivot, start)
        except:
            print('Value error: Not found the pivot element')
            assert False
        start = pivotidx + 1
    print('pivot idx', pivotidx)

    print('After split()', numbers)
    assert numbers[pivotidx] == pivot

    for i in range(pivotidx):
        assert numbers[i] <= pivot

    for i in range(pivotidx + 1, len(numbers)):
        assert numbers[i] > pivot

# assert v1 == -10, "Min value does not match"
# assert v2 == 5, "Max value does not match"
