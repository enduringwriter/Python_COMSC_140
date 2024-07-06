"""
This code demonstrates different mothods of passing arguments to functions,
specifically keyword arguments, dictionary unpacking, and the formatting of output.

**kwargs collects keyword arguments into a dictionary.
** expects a dictionary, and using it with a string will result in an error.

Diciontary Unpacking:
When calling the function, the '**scores' syntax is used to unpack the dictionary.
This passes the key-value pairs in the dictionary as individual keyword arguments.

printscores1 and printscores2 have the same output with the
subject and scores on a new line with right-aligned formatting.
printscores3 outputs the scores on a single line with right-alighed formatting.
"""

def printscores1(**scores):
    """
    printscores1 accepts arbitrary keyword arguments,
    and the dictionary is unpacked in these arguments.
    """
    for k, v in scores.items():
        print(f'Subject {k:>10}: {v:>10}')

def printscores2(scores):
    """
    printscores2 directly accepts a dictionary as its argument.
    """
    for k, v in scores.items():
        print(f'Subject {k:>10}: {v:>10}')


def printscores3(Computer, Math, English):
    print(f'{Math:>10} {English:>10} {Computer:>10}')


def main():
    kwargs = {'Math': 90, 'English': 100, 'Computer': 90}

    print()
    print('printscores1(**kwargs)')
    printscores1(**kwargs)
    print()
    
    print('printscores2(kwargs)')
    printscores2(kwargs)
    print()

    print('printscores3(**kwargs)')
    printscores3(**kwargs)
    print()

if __name__ == '__main__':
    main()
