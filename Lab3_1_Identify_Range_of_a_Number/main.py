def main():
    """
    Identify the range of an inputed number.
    """

    number = int(input('Enter your input: '))

    if number < 50:
        range = 1
    elif number >= 100:
        range = 3
    else:
        range = 2

    # alternative solution
    # range = (1, 2, 3)[(number >=50) + (number >= 100)]

    print(f'Range is {range}')
    ########################################
    # Do not delete the return statement
    ########################################
    return range


if __name__ == '__main__':
    main()
