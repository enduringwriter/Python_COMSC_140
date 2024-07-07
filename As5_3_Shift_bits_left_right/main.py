def shiftN(stringvalue, direction, N):
    """
    Shift the binary string value by N bits to the left or right.
    Add padding 0s to the right or left based on the direction.
    direction of 0 = shift left, 1 = shift right.
    """
    
    if direction == 0:  # shift left
        stringvalue = stringvalue[N:] + '0' * N
    elif direction == 1: # shift right
        stringvalue = '0' * N + stringvalue[:-N]
    return stringvalue


def main():
    str = '001100'
    print(int(str, 2))
    rstr = shiftN(str, 0, 2)
    print(rstr)
    print(int(rstr, 2))

    rstr = '110000'
    rstr = shiftN(rstr, 1, 4)
    print(rstr)
    print(int(rstr, 2))


if __name__ == '__main__':
    main()
