import random
"""
Find the smallest number.
"""

def main():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    number3 = random.randint(0, 100)
   
    if number1 <= number2 and number1 <= number3:
        min_value = number1
    elif number2 <= number1 and number2 <= number3:
        min_value = number2
    else:  # number3 is the smallest
        min_value = number3

    print(f'The three numbers are: {number1}, {number2}, {number3}. The smallest number is: {min_value}')

    ########################################
    # Do not delete the return statement
    ########################################
    return number1, number2, number3, min_value


if __name__ == '__main__':
    main()
