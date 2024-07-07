import random
import main


def test_lambda0():
    c = '\t'
    ret = main.isspace(c)
    print('Your result :', ret)
    assert ret == True
    c = '\n'
    ret = main.isspace(c)
    print('Your result :', ret)
    assert ret == True


def test_lambda1():

    strval = 'Python Programming Section 1'
    ret = main.mystrip(strval)
    print('Your result :', ret)

    assert ret == 'PythonProgrammingSection1'


def test_lambda2():
    strval = 'Python     Programming C++     '
    ret = main.mystrip(strval)
    print('Your result :', ret)

    assert ret == 'PythonProgrammingC++'
