def main():
    """
    This program outputs a list of the remainder of dividing a number by 2 continually
    until the dividend is less than 2. The number is inputted by the user.
    """
    
    result = []
    
    while True:
        try:
            number = int(input('Enter an integer greater than 1: '))
            if number <= 1:
                print('Enter an integer greater than 1.')
                continue  # Ask for input again
            break  # Exit the loop if input is valid
        except ValueError:
            print('Invalid input. Please enter a valid integer.')  # Ensures the input is an integer

    while number >= 2:
        result.append(number % 2)
        number = number // 2

    result.append(number)  # Add the last number which is less than 2

    print(*result)

    return result

if __name__ == '__main__':
    main()
