"""
* operator is used to allow a function to accept an arbitrary number of arguments.
*args collects positional arguments into a tuple

using '*' with a string unpacks the string into individual characters when passed
to a function that collects then into a tuple.

In example 1 of printfunction1, 'str' output separates characters individually
becauase '*' creates a tuple for each letter in the string.

In example 4 of printfunction1, each arguement becomes an element in the tuple.
This explains why each argument is separated as opposed to output in example 1.

In examples 2 and 3: a tuple is created in example 2,
while in example 3, the string retains its string property
"""

def printfunction1(*str):
    print(str)
    for v in str:
        print(v, end=' ')
    print()


def printfunction2(str):
    print(str)
    for v in str:
        print(v, end='')
    print()


def main():
    str = 'Python Programming'
    
    print()
    print('1')
    printfunction1(*str)

    print()
    print('2')
    printfunction1(str)

    print()
    print('3')
    printfunction2(str)

    print()
    print('4')
    morestr = 'C++ Programming'
    printfunction1(str, morestr)
    # printfunction2(str, morestr)  # Error


if __name__ == '__main__':
    main()
