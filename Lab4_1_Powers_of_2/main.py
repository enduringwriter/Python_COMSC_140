def main():
    """
    The purpose of this program is to use a For Loop to generate and store all powers of 2 from 0 to N in a list.
    Where N is a user input.
    """

    N = int(input("Enter a number, 'N', and get the power of 2 from 0 to N in a list: "))
    result = [0] * (N + 1) # pre-allocated List, good if you know the size of the list
    # result = []  # if using append method, you don't need to pre-allocate the list
    
    # Difference between pre-allocated and append method
    # pre-allocated is faster than append method but requires you to know the size of the list
    
    for i in range(N + 1):
        result[i] = 2**i
        # result.append(2**i)
    
    print(f'You entered {N}. The powers of 2 from 0 to N are: {result}')
    
    return result


if __name__ == '__main__':
    main()