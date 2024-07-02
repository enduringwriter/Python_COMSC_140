"""
Learn id() function values and defining usable functions. 
"""

def getinput(n1, n2):
    print('At function start id n1', id(n1))
    print('At function start id n2', id(n2))
    # Num1 and num2 both print the same ID as there is no change, both are the same value.

    n1 = input('Enter a number')
    n2 = input('Enter a number')
    
    print('At function end id n1', id(n1))
    print('At function end id n2', id(n2))
    # The IDs are not the same because the values of n1 and n2 are not the same,
    # unless the user enters the same value i.e. '3' for both n1 and n2.

def main():
    num1 = num2 = 0
    
    print('Before call function id n1', id(num1))
    print('Before call function id n2', id(num2))
    # Num1 and num2 both print the same ID b/c both are assigned the same value '0'.

    getinput(num1, num2)  # these values are not be assigned and thus the code ends here.
 
    print('After call function id n1', id(num1))
    print('After call function id n2', id(num2))
    print(num1, num2)
    # Nothing changes here, as the values from getinput were not assigned,
    # therefore num1 and num2 are still assigned the same value '0'.

    return num1, num2
    # This return statement may be ignored as the values num1 and num2 are not being used anywhere.


if __name__ == '__main__':
    main()
