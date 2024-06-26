import random

def main():
    """
    This program generates random numbers in a list until the sum is greater than 100.
    The sum and the random numbers before breaking 100 are are printed.
    
    Assumption: Random number is an integer from 0 to 100, inclusive.
    """
    
    total = 0
    numbers = []

    while total <= 100:
        number = random.randint(0,100)
        numbers.append(number)
        total += number

    total = total - numbers[-1]
    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    return numbers, total


if __name__ == '__main__':
    main()
