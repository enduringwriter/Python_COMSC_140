import random

def merge(number1, number2):
    """
    Merge two sorted lists into a single sorted list.
    
    temp_number1 = number1[:] results in a duplication.
    temp_number1 = number1 results in a reference.
    """
    # mlist = []
    temp_number1 = number1[:]  # Duplicate number1 to temp_number1
    temp_number2 = number2[:]  # Duplicate number2 to temp_number2
    i = 0
    while temp_number1:  # Loop until all elements from temp_number1 are merged into temp_number2
        while i < len(temp_number2) and temp_number2[i] <= temp_number1[0]:  # i is the index of temp_number2, and temp_number2[i] is the element to compare with temp_number1[0]
            i += 1
        temp_number2.insert(i, temp_number1.pop(0))  # insert smaller number from temp_number1 into temp_number2
        i += 1
    print('\nnumber1:', number1, '\nnumber2:', number2, '\ntemp_number1:', temp_number1, '\ntemp_number2:', temp_number2)
    return temp_number2


def main():
    number1 = [0, 2, 3]
    number2 = [1, 4, 5, 6, 9]
    retlist = merge(number1, number2)
    print(retlist)
    # #########################################

    # n1 = [random.randint(0, 20) for i in range(5)]
    # n2 = [random.randint(0, 20) for i in range(3)]
    # n1.sort()
    # n2.sort()
    # print(n1)
    # print(n2)
    n1 = [1, 3, 5]
    n2 = [2, 4, 6, 8, 10]
    retlist = merge(n1, n2)
    print(retlist)


if __name__ == '__main__':
    main()
