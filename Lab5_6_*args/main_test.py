
import main


def test_main():
    str = 'Python Programming'
    main.printfunction1(*str)
    main.printfunction2(str)

    morestr = 'C++ Programming'
    assert main.printfunction1(str, morestr) == None
    assert main.printfunction1('a', 'b', 'c', 'd', 'e') == None
    # assert v1 == -10, "Min value does not match"
    # assert v2 == 5, "Max value does not match"
