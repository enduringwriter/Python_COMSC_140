import math

def main():
    """
    This program will take two inputs from the user and return a list of prime numbers between those two inputs.
    Both values must be integers greater than 1 and the first value must be less than the second value.
    
    Prime numbers are natural numbers that are divisible only by 1 and themselves.
    The conditions for a number to be prime are:
    It must be greater than 1.
    It must not be divisible by any number from 2 up to the integer part of its square root.

    Example: Is 121 prime?
    
    Condition 1:
    The number, 121, is greater than 1.
    
    Condition 2:
    The floor of the square root of 121 is 11, so the range is 2 to 11.
    121 / 2 = 60.5 meaning 121 is not divisible by 2.
    121 / 3 ...
    121 / 11 = 11 meaning 121 is divisible by 2. Thus, 121 is not a prime number.
    """
    
    while True:
        try:
            begin = int(input('Enter the value for begin: '))
            end = int(input('Enter the value for end: '))
            if begin <=1 or end <=1 or begin >= end:
                print("Please enter valid entries where both values are greater than 1 and 'begin' is less than 'end'.")
                continue
        except ValueError:
            print('Please enter a valid integer')
            continue
        else:
            break
    
    plist = []
    for number in range(begin, end + 1):  # include 'end' in the range
        numbers_to_divide = int(math.sqrt(number))
        for i in range(2, numbers_to_divide + 1):  # include the last number in the range
            if number % i == 0:
                break  # number is not a prime number
        else:
            plist.append(number)

    print(*plist)

    return plist


if __name__ == '__main__':
    main()
