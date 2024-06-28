def main():
    """
    The purpose of this program is to find the least and greatest values among 5 user input values
    and save these values to the list ‘numbers’.
    Assumption: The instructor is asking us to write the code for whole numbers.
    """

    numbers = [0]*5
    maxval = float('-inf')  # Initialize to the smallest possible number
    minval = float('inf')   # Initialize to the largest possible number
    
    for _ in range(len(numbers)):
        number = int(input('Enter an integer: '))
        numbers[_] = number
        if number > maxval:
            maxval = number
        if number < minval:
            minval = number     

    print(*numbers)
    print(maxval, minval)
    
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
