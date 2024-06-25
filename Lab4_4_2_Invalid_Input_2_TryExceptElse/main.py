def main():
    """
    This program will prompt the user for an integer and validate the input.
    Once valid, exit the loop and print and return the number.
    """
    
    while True:
        try:
            number = int(input('Enter an integer: '))
        except ValueError:
            print('That is not an integer. Please try again.')
            continue
        else:
            print(number)
            break
        
    return number


if __name__ == '__main__':
    main()
