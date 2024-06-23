def main():
    """
    This program evaluates a user inputted email address.
    The email length must be greater than 5 and less than 30, and include the '@' symbol.
    The email address must begin with an alphabet character, which can be upper or lower case.
    Email address must include at least one '.' after '@'.
    """

    email = input('Enter your email: ')
    
    count_at_symbol = email.count('@')
    find_at_symbol_index = email.find('@')
    email_sliced_after_at = email[find_at_symbol_index + 1:]
    count_dot_symbol_after_at = email_sliced_after_at.count('.')

    if not(5 < len(email) < 30) or count_at_symbol != 1 or count_dot_symbol_after_at != 1 \
        or email[0] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        result = False
    else: 
        result = True
    
    print(f'Email address entered: {email}. Email address validity: {result}.')

    return result


if __name__ == '__main__':
    main()
