def encrypt(strval, indices):
    """
    This program takes a string as a list and indices as a list,
    and rearranges the original string to an encrypted string
    based on the indices.

    Assumptions: The lengths of the string value and indices are the same.
    """

    encrypted_string = ['']*len(strval)
    encrypted_string_joined = ''
    for i, index in enumerate(indices):
        encrypted_string[index] = strval[i]

    for letter in encrypted_string:
        encrypted_string_joined += letter

    print(encrypted_string_joined)
    return encrypted_string_joined
    


def main():
    strval = 'Python'
    indices = [1, 2, 3, 4, 5, 0]
    ret = encrypt(strval, indices)
    print(f'Your return value: {ret}')

    strval = 'Python'
    indices = [3, 4, 1, 2, 5, 0]
    ret = encrypt(strval, indices)
    print(f'Your return value: {ret}')

    strval = 'Python'
    indices = [0, 5, 1, 2, 3, 4]
    ret = encrypt(strval, indices)
    print(f'Your return value: {ret}')


if __name__ == '__main__':
    main()
