import random

def getRandom(N):
    """
    Generate N random numbers from 0 to 100, inclusive.
    """
    randnums = []
    # for i in range(N):
    #     randnums.insert(i, random.randint(0,100))
    randnums = [random.randint(0,100) for i in range(N)]  # list comprehension
    return randnums


def findMin(numbers):
    """
    Find the minimum nunber in a list of numbers
    and swap it with the first element in the list.
    """
    minimum_num_index = numbers.index(min(numbers))
    numbers[minimum_num_index], numbers[0] = numbers[0], numbers[minimum_num_index]
    return numbers


def main():
    N = 5
    numbers = getRandom(N)
    print(f'The original list values : { numbers }')
    findMin(numbers)
    print(f'The list values after findMin() : { numbers }')


if __name__ == '__main__':
    main()
