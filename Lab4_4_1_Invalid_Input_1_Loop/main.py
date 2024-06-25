def main():
    """
    This program will prompt the user for a valid integer using while loop.
    Valid condition: 0 < number < 100.
    Once valid exit the loop, and print and return the number.
    
    Assumption: User will enter integers only and no invalid entries like floats and alphabet characters.
    Otherwise, the code will break.
    """

    number = -1
    
    while (number <= 0 or number >= 100):
        number = int(input("Please enter a valid integer greater than 0 and less than 100: "))
    print(number)

    return number


if __name__ == '__main__':
    main()
