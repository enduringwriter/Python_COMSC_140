def main():
    """
    This program uses an if conditions algorithm to reorder numbers in ascending order.
    """
    
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    
    if num1 <= num2 <= num3:
        minval, median, maxval = num1, num2, num3
    elif num1 <= num3 <= num2:
        minval, median, maxval = num1, num3, num2
    elif num2 <= num1 <= num3:
        minval, median, maxval = num2, num1, num3
    elif num2 <= num3 <= num1:
        minval, median, maxval = num2, num3, num1
    elif num3 <= num1 <= num2:
        minval, median, maxval = num3, num1, num2
    else:
        minval, median, maxval = num3, num2, num1
    
    print(minval, median, maxval)

    return minval, median, maxval


if __name__ == '__main__':
    main()