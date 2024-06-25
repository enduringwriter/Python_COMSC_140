import random

def main():
    """
    This program uses the while loop to generate 5 random numbers and caculates the total of the numbers.
    """

    # while loop
    numbers = [0] * 5
    while True:
        for _ in range(len(numbers)):
            numbers[_] = random.randint(0, 100)
        break
   
   
    # for loop
    # numbers = [0] * 5
    # for _ in range(len(numbers)):
    #     numbers[_] = random.randint(0, 100)  # includes 0 and 100, inclusive
    
    
    # list comprehension
    # numbers = [random.randint(0, 100) for _ in range(5)]
    
    
    total = sum(numbers)
    
    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    return numbers, total


if __name__ == '__main__':
    main()
