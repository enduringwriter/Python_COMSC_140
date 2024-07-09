"""
.sort() and sorted()
sort is a stable method that preserves the order of applications.
"""

def findNames(names):
    """
    Find the longest and shortest strings in a list. If there are multiple names
    of the same length, find the least in alphabetical order.
    """
    names.sort()  # sort alphabetically
    names.sort(key=len)  # sort by length; alphabetical order is preserved    
    longest = names[-1]
    shortest = names[0]
    return longest, shortest


def main():

    # names = input('Enter 5 students names').split()
    names = ['Albert', 'Joanne', 'Kurt', 'Bill', 'Matt']

    longest, shortest = findNames(names)

    print('The shortest name is ', shortest)
    print('The longest name is ', longest)


if __name__ == '__main__':
    main()
