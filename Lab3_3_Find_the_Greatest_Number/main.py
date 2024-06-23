def main():
    """
    Find the greatest number.
    """

    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))

    if num1 >= num2 and num1 >= num3:
        maxnum = num1
    elif num2 >= num1 and num2 >= num3:
        maxnum = num2
    else:
        maxnum = num3

    print(f'The greatest number is {maxnum}')

    return maxnum

if __name__ == '__main__':
    main()
