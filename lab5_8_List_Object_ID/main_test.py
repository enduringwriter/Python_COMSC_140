
import main
import main1_page39 as main1
import main2_page39 as main2


def test_main():
    n = [1, 2, 3]
    ret = main.myfunc(n)
    assert id(n) == id(ret)


def test_main_page39():
    numbers = [5, 4, 3, 2, 1]

    others = main1.myfunc(numbers)
    assert id(numbers) == id(others)

    first, *others = main2.myfunc(numbers)
    print(others)
    assert id(numbers) != id(others)


# assert v1 == -10, "Min value does not match"
# assert v2 == 5, "Max value does not match"
