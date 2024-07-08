def getInput():
    """
    Get integers from user in a single line.
    Split the values and conver them into a list of integers, and return it.
    """
    return list(map(int, input("Enter a list of numbers. Press 'enter' when done.").split()))


def makeReverse(numbers):
    """
    Create a new list of numbers in rev order without using rev function.
    """
    new_numbers = []
    for n in numbers:
        new_numbers.insert(0, n)
    return new_numbers


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
