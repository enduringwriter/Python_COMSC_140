
def isSubset(num1, num2):
    """
    This program checks if one list is a subset of another,
    if the subset is in the same sequence without any broken sequence. 
    
    Example:
    num1 = [2, 3]
    num2 = [4, 7, 2, 3, 12]
    num1 is a subset of num2
    """

    len_num1 = len(num1)
    for i in range(len(num2)):
        end_index = i + len_num1
        num2_slice_to_check = num2[i:end_index]  # comparision test to num2

        if num2_slice_to_check == num1:
            is_sublist = True
            break  # prevent is_sublist from being overwritten; exit loop if subset is found
        else:
            is_sublist = False
    return is_sublist

def main():
    num1 = [20, 30, 35]
    num2 = [5, 20, 30, 35, 50]
    ret = isSubset(num1, num2)
    print(f'Your return value is {ret}')  # True

    num1 = [1, 3, 2]
    num2 = [1, 2, 3, 4, 5]
    ret = isSubset(num1, num2)
    print(f'Your return value is {ret}')  # False

    num1 = [1, 4, 5]
    num2 = [1, 2, 3, 4, 5]
    ret = isSubset(num1, num2)
    print(f'Your return value is {ret}')  # False

    num1 = [1, 3, 2]
    num2 = [4, 1, 3, 2, 5]
    ret = isSubset(num1, num2)
    print(f'Your return value is {ret}')  # True


if __name__ == '__main__':
    main()
