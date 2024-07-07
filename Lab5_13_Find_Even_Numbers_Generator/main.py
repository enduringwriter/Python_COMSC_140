import random


def findEvenNumber(numbers):
    """
    Create a generator function that yields all the even numbers from a given list of integers.
    Generators and the `yield` statement, allows for efficient memory usage by generating values on the fly without storing the entire sequence in memory.
    """

    for i in numbers:
        if i%2==0:
            yield i  # yield  creates a generator object that interates over the list of numbers and returns the even numbers
            
    #  no return statement needed as the generator function will automatically return a generator object


def main():
    numbers = [random.randint(0, 100) for i in range(10)]
    print('Original list', numbers)
    gen = findEvenNumber(numbers)

    for i in gen:
        print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
