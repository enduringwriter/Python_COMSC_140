import random

greater = lambda x, y: max(x,y)

filter50 = lambda numbers: [i for i in numbers if i > 50]

"""
This program uses two lamda functions.
The first determines the max of two numbers.
The second accepts a list of numbers and returns a new list containing numbers >50.
"""


def main():
    print(greater(10, 20))
    print(greater(20, 10))
    print(greater(100, 20))

    numbers = [random.randint(0, 100) for i in range(10)]
    print('original list', numbers)
    print('filter 50', filter50(numbers))


if __name__ == '__main__':
    main()
