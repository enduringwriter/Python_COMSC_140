
import main


def test_main():

    kargs = {'Math': 90, 'English': 100, 'Computer': 90}
    assert main.printscores1(**kargs) == None
    assert main.printscores2(kargs) == None
    assert main.printscores3(**kargs) == None

    # assert v1 == -10, "Min value does not match"
    # assert v2 == 5, "Max value does not match"
