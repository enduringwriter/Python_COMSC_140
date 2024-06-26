def main():
    """
    This program prints the consecutive letters from 'start' to 'end'
    that are inputted by the user as single digit strings.
    """

    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the end letter: ')
        if not(ord(end) >= ord(start) and start.isalpha() and end.isalpha() and start.islower() and end.islower()):
            print('Enter a valid letter.')
        else:
            for i in range (ord(start), ord(end) + 1):
                result.append(chr(i))
            break  # Break out of the loop after successfully processing the inputs

    print(*result)

    return result


if __name__ == '__main__':
    main()
