def shuffle(num1, num2):
    """
    This program shuffles two lists by alternating elements from each list.
    Once a list is exhausted, remaining elements from the other list, if any,
    are copied to the end of the result.
    """
    shuffle = []
    i, j = 0, 0

    while i < len(num1) and j < len(num2):
        shuffle.append(num1[i])
        shuffle.append(num2[j])
        i += 1
        j += 1
    
    # Copy remaining elements from the first list, if any
    # No while or for loop, or if statement is needed because
    # all elements are copied rather than one by one as a loop would do.
    shuffle.extend(num1[i:])
    shuffle.extend(num2[j:])

    return shuffle


def main():
    num1 = [1, 2, 3]
    num2 = [4, 5, 6, 7]
    ret = shuffle(num1, num2)
    print(f'The return value is: {ret}')

    num1 = [1, 2, 3, 4, 5]
    num2 = [6, 7, 8]
    ret = shuffle(num1, num2)
    print(f'The return value is: {ret}')
##


if __name__ == '__main__':
    main()
