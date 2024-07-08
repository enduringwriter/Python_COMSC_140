"""
The map() function executes a specified function for each item in an iterable.
The item is sent to the function as a parameter.
Syntax: map(function, iterables)

Dictionary syntax requires brackets, [] to set and access keys and values.

list methods: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
"""

def getInput():
    """
    Prompt the user to enter multiple values in a single line.
    Then split the values and convert them into a list of integers, and return it.
    """
    str_input = input("Enter a list of numbers in a single entry. When done, press enter.")
    numbers = list(map(int, str_input.split()))
    return numbers


def findMost(numbers):
    """
    Find the mode in the list of numbers and return it.
    """
    frequency = {}
    for n in numbers:
        frequency[n] = numbers.count(n)  # use brackets to set and access keys and values within a dictionary
    most_common = max(frequency, key=frequency.get)  # .get returns the value (count) for a key (number)
    return most_common

def main():
    numbers = getInput()
    ret = findMost(numbers)
    print(f'The most frequently used numbers is: {ret}')


if __name__ == '__main__':
    main()
