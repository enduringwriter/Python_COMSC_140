import random
import main


def test_sumProduct1():

    numbers1 = [5, 3, 1, 1, 2]
    numbers2 = [1, 2, 2, 9, 5]
    print('numbers 1 ', numbers1)
    print('numbers 2 ', numbers2)
    result = main.sumoProduct(numbers1, numbers2)
    print('Your result is: ', result)

    assert result == 32, "Invalid value. Expected 32"


def test_sumProduct2():
    numbers1 = [random.randint(1, 10) for i in range(5)]
    numbers2 = [random.randint(1, 10) for i in range(5)]
    sumP = 0
    for i in range(5):
        sumP += numbers1[i] * numbers2[i]
    print('numbers 1 ', numbers1)
    print('numbers 2 ', numbers2)
    result = main.sumoProduct(numbers1, numbers2)
    print('Your result : ', result)
    assert result == sumP, "Invalid value."
