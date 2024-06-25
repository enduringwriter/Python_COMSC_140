def main():
    """
    This program calculates the running total from a list of numbers.
    The numbers are entered by the user.
    """
      
    total = 0
    numbers = [0] * 5
    
    for i in range(len(numbers)):
        number = int(input("Enter a number: "))
        numbers[i] = number
        total += number
    print(f'The numbers are: {numbers}. The total is: {total}')
    
    return total, numbers


if __name__ == '__main__':
    main()
