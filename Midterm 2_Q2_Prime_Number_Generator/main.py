import math

"""
This program generates prime numbers between a specified range
using a generator function. Yield is used to return the prime number
and iterate the for loop.
"""

def isPrime(number):
    if number < 2:
        return False
    numbers_to_divide = int(math.sqrt(number))
    for i in range(2, numbers_to_divide + 1):
        if number % i == 0:
            return False  # number is not a prime number
    else:
        return True


def getPrimeNumber(begin, end):
    for i in range(begin, end):
        if isPrime(i):
            yield i


def main():
    begin = int(input('Enter the number for starting of range: '))
    end = int(input('Enter the number for end of range: '))
    gen = getPrimeNumber(begin, end)

    print(list(gen))


if __name__ == '__main__':
    main()
