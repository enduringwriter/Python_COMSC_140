def getFarNumber(numbers):
    """
    Find the number that has the greatest gap from the average.
    """
    avg = sum(numbers)/len(numbers)
    diff, max_diff, max_num = 0, 0, 0
    
    for num in numbers:
        diff = abs(num - avg)
        if diff > max_diff:
            max_diff = diff
            max_num = num
    return max_num


def main():
    numbers = [10, 5, 20, 0, 40, 45, 50, 55, 9, 10]
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
    ret = getFarNumber(numbers)
    print(f'Your return value is {ret}')
    ##################################################
    # Code your program here
    ##################################################


if __name__ == '__main__':
    main()
