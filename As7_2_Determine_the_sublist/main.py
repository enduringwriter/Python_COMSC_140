def isSubList(numbers1, numbers2):
    """
    This program determines if a list is a sublist of another list.
    """
    is_sublist = False

    for num in numbers1:
        for i in numbers2:
            if num == i:
                is_sublist = True
                break
        else:
            is_sublist = False
        # alternative to use else statement
        # if not is_sublist:
            # return False
    return is_sublist

def main():
    numbers1 = [40, 10, 5]
    numbers2 = [10, 5, 20, 0, 40, 45, 50]

    if isSubList(numbers1, numbers2):
        print(f'{numbers1} is a Sublist of {numbers2} ')
    else:
        print(f'{numbers1} is not a Sublist of {numbers2} ')


if __name__ == '__main__':
    main()
