"""
map(function, iterables) where function is being executed for each item.
"""

def getInput():
    """
    Get a list of integers from the user, then split and convert str input to int values.
    """
    return list(map(int, input("Enter values in one line. Press 'enter' when done. ").split()))

def evenList(numbers):
    """
    Extract the list of numbers that are even-indexed from the original list, so that
    the original list has the odd-indexed numbers.
    """

    even_numbers, odd_numbers = [], []
    even_numbers = [numbers[i] for i in range(0, len(numbers), 2)]
    odd_numbers = [numbers[i] for i in range(1, len(numbers), 2)]
    numbers[:] = odd_numbers
    return even_numbers

def main():
    numbers = getInput()
    retval = evenList(numbers)
    print(f'The numbers at the even index: {retval}')
    print(f'The remainder numbers in the original list: {numbers}')


if __name__ == '__main__':
    main()
