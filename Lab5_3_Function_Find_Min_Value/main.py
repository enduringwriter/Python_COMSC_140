import random


def mineven(numbers):
    """
    Determine the minimum even number in a list, extract it,
    and print the min even number and the updated list.
    """
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    minval = min(even_list)

    if even_list:
        return minval
    else:
        return None


def main():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = mineven(numbers)
    numbers.remove(result)
    # del numbers[numbers.index(result)]
    print(numbers)
    print(result)

    numbers = [1, 3, 5, 7, 10, 14, 2, 8]
    result = mineven(numbers)
    numbers.remove(result)
    # del numbers[numbers.index(result)]
    print(numbers)
    print(result)

    N = random.randint(5, 20)
    numbers = [random.randint(-50, 50) for v in range(N)]
    print(numbers)
    result = mineven(numbers)
    numbers.remove(result)
    # del numbers[numbers.index(result)]
    print(numbers)
    print(result)


if __name__ == '__main__':
    main()
