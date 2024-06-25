def main():
    """
    This program will prompt the user for an integer > 0 and < 100, and validate the input.
    Once valid, exit the loop and print and return the number.
    """
    
    while True:
        try:
            number = int(input('Enter an integer: '))
            if number <= 0 or number >= 100:
                print('You entered an invalid integer. Please try again.')
                continue
        except ValueError:
            print('That is not a valid entry. Please try again.')
            continue
        else:
            print('Your valid integer is: ', number)
            break

    # alternative solution
    # while True:
    #     try:
    #         number = int(input("Enter an integer: "))
    #         if number <= 0 or number >= 100:
    #             print("That's not a valid entry. Please try again.")
    #         else:
    #             break
    #     except ValueError:
    #         print("That's not a valid entry. Please try again.")
    # print('Your valid integer is: ', number)
            
    return number


if __name__ == '__main__':
    main()
