def main():
    """
    Midterm. Question 1.
    This program counts the groups of consecutive even numbers in a list inputted by the user.
    """
    
    number = []
    count_even_numbers = 0
    evencnt = 0
    
    for i in range(10):
        number.append(int(input('Enter a number: ')))
    
    for num in number:
        if num % 2 == 0:
            count_even_numbers += 1       
        else:
            if count_even_numbers >= 2:
                evencnt += 1
            count_even_numbers = 0

    # condition above works if the last digit is odd, if not, and count_even_numbers >= 2,
    # then have to add the final even numbered group.
    if count_even_numbers >= 2:
        evencnt += 1

    print(evencnt)

    return evencnt


if __name__ == '__main__':
    main()
