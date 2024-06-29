import math

def main():
    """
    Midterm 1 Question 3.
    This program finds the next prime number after the given input.
    """

    number = int(input('Enter your number: '))
    pnumber = 0
    
    next_number = number + 1
    
    while True:
        numbers_to_divide = int(math.sqrt(next_number))
        for i in range(2, numbers_to_divide + 1):  # include the last number in the range
            if next_number % i == 0:
                break  # number not prime
        else:
            pnumber = next_number  # found the next prime number
            break
        next_number += 1

    print(f"The next prime number after {number} is: {pnumber}")

    return pnumber

if __name__ == '__main__':
    main()
