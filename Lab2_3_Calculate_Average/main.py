def main():
    """
    Collect three integers from the user, calculate their total and average, and print the results.
    """

    val1 = int(input('Input the first integer: '))
    val2 = int(input('Input the second integer: '))
    val3 = int(input('Input the third integer: '))
    
    total = val1 + val2 + val3
    average = total/3
    
    print(f'The three integers are: {val1}, {val2}, and {val3}')
    print(f'The total is: {total}')
    print(f'The average is: {average}')

    return total, average


if __name__ == '__main__':
    main()
