def getInput():
    """
    Get a list of integers from the user, then split and convert str input to int values.
    """
    return list(map(int, input("Enter values in one line. Press 'enter' when done. ").split()))


def insertOne(numbers):
    """
    Get user insertion value and insert it into the correct index to keep the list ordered.
    """
    userval = int(input('Enter the insertion value: '))
    for i in range(len(numbers)):
        if  userval < numbers[i]:
            numbers.insert(i, userval)
            break  # stop loop once userval is less than an element in the list.
        if userval > max(numbers):
            numbers.append(userval)
            break
    
    # while loop
    # i = 0
    # while i < len(numbers) and userval > numbers[i]:
    #     i += 1
    # numbers.insert(i, userval)
    # while loop has not been tested for the case when userval is greater than max(numbers)


def main():
    numbers = getInput()    # test input: 10 15 25 30 35
    insertOne(numbers)      # test input 20
    print(numbers)         # list value after insertion


if __name__ == '__main__':
    main()
