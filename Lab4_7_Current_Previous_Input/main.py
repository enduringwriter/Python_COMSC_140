def main():
    """
    This program continuallys asks and stores user input in a list
    until the current value is greater than the previous value.
    All input values except the last one should be stored in the list.
    """

    numbers = []
    while True:
        try:
            number = int(input('Enter an integer: '))
        except ValueError:  # occurs if the input is not an integer
            print('Enter a valid integer.')
            continue
        else:  # this if condition block will work without 'else', and is executed only if no exception was rasied.
            if numbers and number > numbers[-1]:  # an empty list results as False
                break
            numbers.append(number)
    print(*numbers)  # output the list without brackets and commas
    return numbers


if __name__ == '__main__':
    main()


# alternative input validation
# def get_valid_integer():
#     while True:
#         try:
#             return int(input('Enter an integer: '))
#         except ValueError:
#             print('Enter a valid integer.')

# def main():
#     numbers = []
#     while True:
#         number = get_valid_integer()
#         if numbers and number > numbers[-1]:
#             break
#         numbers.append(number)
#     print(*numbers)
#     return numbers

# if __name__ == '__main__':
#     main()
