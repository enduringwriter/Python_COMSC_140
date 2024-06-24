def main():
    """
    This program calculates the running total of a list of numbers inputted by the user.
    Use a for loop.
    """

    total = 0
    
    for i in range (0, 5):
        user_input = int(input("Enter a number: "))
        total += user_input
    
    print(total)
    
    return total


if __name__ == '__main__':
    main()
