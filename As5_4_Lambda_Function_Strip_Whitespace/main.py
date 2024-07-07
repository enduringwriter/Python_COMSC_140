"""
This program uses a lambda function to check for whitespace characters (' ', \n, \t)
and uses it to strip whitespace characters from a given string.
"""

items_to_check = [' ', '\t', '\n']
isspace = lambda strval : strval in items_to_check


def mystrip(strval):
    strip = ''
    for v in strval:
        if not isspace(v):
            strip += v
    return strip


strval = 'Python Programming\t Section 1\n'
ret = mystrip(strval)
print(ret)
