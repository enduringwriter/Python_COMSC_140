"""
Lab7_4_Get_Lists_and_Add_Corresponding_Numbers

Notes:
The map() function executes a specified function for each item in an iterable.
The item is sent to the function as a parameter.
Syntax: map(function, iterables)

Dictionary syntax requires brackets, [] to set and access keys and values.

list methods: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
"""

def getInput():
    """
    Prompt the user to enter multiple values in a single line.
    Then split the values and convert them into a list of integers, and return it.
    """
    list1 = list(map(int, input("Enter numbers in a single entry for List1. When done, press enter. ").split()))
    list2 = list(map(int, input("Enter numbers in a single entry for List1. When done, press enter. ").split()))
    return list1, list2


def listSum(list1, list2):
    """
    Sum the corresponding elements of two lists and return the sum list.
    
    zip() function combines 2 or more iterables .e.g. lists, tuples, etc.
    zip() function returns an iterator of tuples where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
    
    lambda function is an anonymous function that can have any number of arguments, but it can only have one expression.
    lambda arguments: expression
    
    map() function executes a specified function for each item in an iterable.
    
    Assumption: The two lists are of the same length.
    """
    sum_list = list(map(lambda i, j: i + j, list1, list2))
    # sum_list = list(map(lambda x: sum(x), zip(list1, list2)))
    # sum_list = [i + j for i, j in zip(list1, list2)]
    
    # import operator
    # sum_list = list(map(operator.add, list1, list2))
    return sum_list

def main():
    list1, list2 = getInput()
    ret = listSum(list1, list2)
    print(f'The sum of the two lists is: {ret}')

if __name__ == '__main__':
    main()
