
def deleteOne(numbers, value):
    """
    This program deletes all occurrences of a specified element from a list.
    """

    try:
        for num in numbers:
            while num == value:
                numbers.remove(value)
                continue
    except ValueError:
        print('Value to remove from list is not found.')        

def main():
    numbers = [5, 20, 30, 30, 35]
    print(f'Original list value: {numbers}')
    deleteOne(numbers, 30)
    print(f'After deleting 30 {numbers}')


if __name__ == '__main__':
    main()
