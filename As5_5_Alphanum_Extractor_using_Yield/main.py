def getalnum(strval):
    """
    Extracts alphanumeric characters from a given string using the yield statement.

    Alphanumeric, in Python, is a string that contains both letter a-z and numbers 0-9.
    """
    for x in strval:
        if x.isalnum():
            yield x


def main():
    strval = 'Python Programming'
    ret = getalnum(strval)
    print(ret)  # print generator information
    retstr = ''.join(ret)

    # retstr = list(ret)
    print(retstr)


if __name__ == '__main__':
    main()
