import main
import io
import sys
import re


def test_main_50():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '50'
    sys.stdin = io.StringIO(datastr)

    rw, ow, tw = main.main()

    sys.stdout = sys.__stdout__
    print('Captured\n', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('730', str(rw))
    assert res != None
    print(res.group())
    res = re.search('277', str(ow))
    assert res != None
    print(res.group())
    res = re.search('1007', str(tw))
    assert res != None
    print(res.group())


def test_main_70():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '70'
    sys.stdin = io.StringIO(datastr)

    rw, ow, tw = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('730', str(rw))
    assert res != None
    assert res.group() == '730', 'Expected 730'
    print(res.group())

    res = re.search('833.4', str(ow))
    assert res != None
    assert res.group() == '833.4', 'Expected 833.4'
    print(res.group())

    res = re.search('1563.4', str(tw))
    assert res != None, 'The final price error'
    assert res.group() == '1563.4', 'Expected 1563.4'
    print(res.group())
