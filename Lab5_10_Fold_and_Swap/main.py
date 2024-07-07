import random
"""
Swap elements that are symmetrically opposite when the list is folded in half.
"""

def foldandswap(numbers):
    max_length = len(numbers)
    for i in range(len(numbers)//2):
        temp = numbers[i]
        numbers[i] = numbers[max_length -i -1]
        numbers[max_length -i -1] = temp


def main():
    numbers = [2, 3, 0, 5, 4, 1, 6, 9, 8, 7]
    print(numbers)
    foldandswap(numbers)
    print(numbers)

    numbers = [random.randint(0, 10) for i in range(10)]
    print(numbers)
    foldandswap(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
