
import main


def test_main():
    numbers = [5, 4, 3, 2, 1]

    print('Test data', numbers)
    main.foldandswap(numbers)
    print('After calling foldandswap()', numbers)
    assert numbers[0] == 1
    assert numbers[1] == 2
    assert numbers[2] == 3
    assert numbers[3] == 4
    assert numbers[4] == 5
# assert v1 == -10, "Min value does not match"
# assert v2 == 5, "Max value does not match"
    numbers = [8, 7, 6, 5, 4, 3, 2, 1]
    print('Test data', numbers)
    main.foldandswap(numbers)
    print('After calling foldandswap()', numbers)
    assert numbers[0] == 1
    assert numbers[1] == 2
    assert numbers[2] == 3
    assert numbers[3] == 4
    assert numbers[4] == 5
    assert numbers[5] == 6
    assert numbers[6] == 7
    assert numbers[7] == 8
