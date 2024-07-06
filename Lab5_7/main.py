"""
Learn how to unpack a list into separate variables using *args.

Identify minimum number in the list and extract it.
Unpack the list with exception to the first element using *args.
Replace the minimum number with the first element in the list.

Return the minimum number and the modified list.
"""

# function without using *args
# def splitlist(numbers):
#     min_num = min(numbers)
#     min_index = numbers.index(min_num)

#     first_num = numbers[0]
    
#     numbers[min_index] = first_num
    
#     numbers.pop(0)
    
#     return min_num, numbers


# function using *args
def splitlist(numbers):
    """
    using args
    """
    first_num, *other_num = numbers
    
    min_num = min(other_num)
    min_index = other_num.index(min_num)
    other_num[min_index] = first_num
    return min_num, other_num

def main():

    numbers = [5, 4, 3, 2, 1]

    first, others = splitlist(numbers)
    print(first)  # Expected output     1
    print(others)  # Expected output     4 3 2 5


if __name__ == '__main__':
    main()
