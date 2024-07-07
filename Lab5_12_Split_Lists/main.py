import random


def split(numbers):
    """
    Split a list of numbers using the first number in the list as the pivot.
    Then compare each element in the list with the pivot.
    Elements <= to pivot will be in the left part of the list.
    Otherwise, elements are put on the right part of the list.
    """
    pivot = numbers[0]
    left, right = [], []
    for n in numbers[1:]:  # Skip the first element
        if n <= pivot:
            left.append(n)
        else:
            right.append(n)
    numbers = left + [pivot] + right  # add pivot as a list, and concatenate the new list
    return numbers


def main():
    numbers = [3, 2, 0, 5, 4]
    # print (id(numbers))
    numbers = split(numbers)
    # print (id(numbers))
    print(numbers)

    numbers = [random.randint(0, 20) for i in range(10)]
    print(numbers)
    numbers = split(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
