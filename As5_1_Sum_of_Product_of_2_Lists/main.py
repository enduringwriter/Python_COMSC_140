import random


def sumoProduct(l1, l2):
    """
    As5_1_Sum_of_Product

    This program receives two lists and returns the sum of the sequential product
    of the respective values in each list.

    Assumption: both lists are the same length.
    """

    return sum([l1[i] * l2[i] for i in range (len(l1))])

def main():
    numbers1 = [5, 3, 1, 1, 2]
    numbers2 = [1, 2, 2, 9, 5]
    result = sumoProduct(numbers1, numbers2)
    print('Your result : ', result)


    numbers1 = [random.randint(1, 10) for i in range(5)]
    numbers2 = [random.randint(1, 10) for i in range(5)]
    print('numbers 1 ', numbers1)
    print('numbers 2 ', numbers2)
    result = sumoProduct(numbers1, numbers2)
    print('Your result : ', result)

if __name__ == "__main__":
    main()