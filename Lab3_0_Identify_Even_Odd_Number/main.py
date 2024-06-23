def main():
    """
    Identify a number as even or odd.
    """

    number = int(input('Enter your input: '))
    if number%2 != 0:
        result = 1
    else:
        result = 0

    if result == 1:
        print(f'The value {number} is an odd number')
    else:
        print(f'The value {number} is an even number')

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()