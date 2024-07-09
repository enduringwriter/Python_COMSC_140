
def findSmallest(numbers, i):
    """
    Find the smallest number and move it to the beginning of the list,
    and replace where the smallet number was (its index) with the largest number.
    """
    smallest = min(numbers)
    largest = max(numbers)
    smallest_index = numbers.index(smallest)
    numbers[smallest_index] = largest
    for x in range(len(i)-1):
        numbers.index(i, smallest)


def selectionSort(numbers):
    """
    ...
    """


def main():
    # numbers = list(map(int, input().split()))
    numbers = [25, 15, 5, 10, 0]
    findSmallest(numbers, 0)
    print(f'Find the 1st smallest number: {numbers}')

    findSmallest(numbers, 1)
    print(f'Find the 2nd smallest number: {numbers}')

    findSmallest(numbers, 2)
    print(f'Find the 3rd smallest number: {numbers}')

    findSmallest(numbers, 3)
    print(f'Find the 4th smallest number: {numbers}')

    findSmallest(numbers, 4)
    print(f'Find the 5th smallest number: {numbers}')
    # Code your program here

    numbers = [25, 15, 5, 10, 0]
    selectionSort(numbers)
    print(f'After call selectionSort(): {numbers}')


if __name__ == '__main__':
    main()
