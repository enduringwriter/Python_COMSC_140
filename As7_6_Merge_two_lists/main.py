def mergeList(num1, num2):
    """
    This program merges two sorted lists into
    a new single sorted list without using sort functions.

    Assumptions: Inputted lists are sorted.
    """

    merged = []
    x, y = 0, 0
    while x < len(num1) and y < len(num2):
        if num1[x] <= num2[y]:
            merged.append(num1[x])
            x += 1
        else:
            merged.append(num2[y])
            y += 1

    #Add remaining elements, if applicable, as loop above stops once one list is exhausted
    while x < len(num1):
        merged.append(num1[x])
        x += 1
    
    for num in range(y, len(num2)):
        merged.append(num2[num])

    return merged

def main():
    num1 = [1, 3, 5, 7]
    num2 = [2, 4, 6, 8]
    merged = mergeList(num1, num2)
    print(f'The merged list is {merged}')

    num1 = [1, 2, 3, 4]
    num2 = [5, 6, 7, 8]
    merged = mergeList(num1, num2)
    print(f'The merged list is {merged}')

    num1 = [5, 10, 25, 75, 85]
    num2 = [45, 55, 60]
    merged = mergeList(num1, num2)
    print(f'The merged list is {merged}')


if __name__ == '__main__':
    main()
