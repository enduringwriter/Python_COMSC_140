import types
import random
import main


def test_main():

    numbers = [random.randint(0, 100) for i in range(10)]
    print('Original list', numbers)
    evenlst = [v for v in numbers if v % 2 == 0]
    cnteven = len(evenlst)

    gen = main.findEvenNumber(numbers)
    resultlst = list(gen)
    print('The number of elements in your result', len(resultlst))
    print(resultlst)
    for i in gen:
        print(i, end=' ')

    assert cnteven == len(
        resultlst), "The number of even elements are incorrect"
#     assert cnteven == 7, "The number of even elements are incorrect."


def test_type_generator():
    numbers = [random.randint(0, 100) for i in range(10)]
    print('Original list', numbers)
    evenlst = [v for v in numbers if v % 2 == 0]
    cnteven = len(evenlst)

    gen = main.findEvenNumber(numbers)
    assert isinstance(gen, types.GeneratorType), 'Your Returned value is not a generator'


def test_yield():
    with open('main.py') as f:
        flag = False
        for line in f:
            if 'yield' in line:
                flag = True
                break

    assert flag == True
