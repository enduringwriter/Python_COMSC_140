import random
import main
import types


def test_lambda1():

    strval = 'Python Programming'
    ret = main.getalnum(strval)
    # ret = main_sol.getalnum(strval)
    print('Your result: ', ret)
    assert type(ret) == types.GeneratorType, 'Return type is not a generator type'
    retstr = ''.join(ret)
    # retstr = list(ret)
    print('Your result ', retstr)

    assert retstr == 'PythonProgramming'


def test_lambda2():
    strval = 'Python     Programming C++     '
    ret = main.getalnum(strval)
    print('Your result: ', ret)
    assert type(ret) == types.GeneratorType, 'Return type is not a generator type'
    # retstr = list(ret)
    retstr = ''.join(ret)
    print('Your result :', retstr)

    assert retstr == 'PythonProgrammingC'
