"""
Sum a given list of numbers excluding the maximum and minimum number.
"""

def getSum(numbers):
    # max_num = max(numbers)
    # min_num = min(numbers)
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    return sum(numbers)


def main():
    numbers = [10, 25, 15, 35, 50]
    total = getSum(numbers)
    print('The total withtou min and max', total)


if __name__ == '__main__':
    main()
