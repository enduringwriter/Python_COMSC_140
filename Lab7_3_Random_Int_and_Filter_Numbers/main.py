import random
"""
Lists methods: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
"""


def getRandom(N):
    """
    Generate N randon integers from 0 to 100, inclusive,
    and return those numbers as a list.
    """
    return [random.randint(0,100) for i in range(N)]


def filterAvg(numbers):
    """
    Filter numbers that are greater than the average of the random numbers,
    and return the filtered numbers as a list.
    """
    filtered_numbers = []
    ave_of_nunbers = sum(numbers)/len(numbers)
    for n in numbers:
        if n > ave_of_nunbers:
            filtered_numbers.append(n)
    return filtered_numbers

def main():
    N = 5
    numbers = getRandom(N)
    print(f'The original list values : { numbers }')
    ret = filterAvg(numbers)
    print(f'The average value: {sum(numbers)/len(numbers)}')
    print(f'The return values from filterAvg() : { ret }')


if __name__ == '__main__':
    main()
