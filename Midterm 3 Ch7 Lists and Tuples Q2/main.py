import random

def getSum(numbers, n):
    """
    This program finds the great summation of n numbers given a
    list of numbers, numbers, and the number of sequences, n.
    """
    # the following passed 4 but failed 2
    # b/c I sorted them rather than getting the consecutive numbers
    # numbers.sort()
    # numbers.reverse()
    # # print('sort: ', numbers)
    # return sum(numbers[0:n])

    max_sum = float('-inf')

    for i in range(len(numbers) - n + 1):
        current_sum = sum(numbers[i:i+n])
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


def main():
    numbers = [3, 8, 9, 6, 5]
    print(numbers)
    ret = getSum(numbers, 3)
    print(f'Your return value: {ret}')

    numbers = [1, 2, 3, 4, 5]
    print(numbers)
    ret = getSum(numbers, 3)
    print(f'Your return value: {ret}')

    numbers = [5, 4, 3, 2, 1]
    print(numbers)
    ret = getSum(numbers, 5)
    print(f'Your return value: {ret}')

    numbers = [5, 4, 3, 2, 1]
    print(numbers)
    ret = getSum(numbers, 1)
    print(f'Your return value: {ret}')

    numbers = [random.randint(-50, 50) for _ in range(10)]
    print(numbers)
    ret = getSum(numbers, 5)
    print(f'Your return value: {ret}')


if __name__ == '__main__':
    main()
