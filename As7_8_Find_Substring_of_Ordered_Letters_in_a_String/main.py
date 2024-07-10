def hasARE(words):
    """
    This program finds words that contain the letters 'a', 'r', and 'e' in sequence.
    
    Assumptions: string input is lowercase, and algorithm checks for lowercase only
    """
    
    are = ['a', 'r', 'e']
    result = []

    # for word in words:
    #     check_subset = 0
    #     for character in word:
    #         if character == are[check_subset]:
    #             check_subset += 1
    #             if check_subset == len(are):
    #                 result.append(word)
    #                 break  # end program once subset is found to prevent further iteration
    
    # alternate solution using .find()
    for word in words:
        check_subset = 0
        for char in are:  # or can use: for char in 'are':
            check_subset = word.find(char, check_subset)
            if check_subset == -1:
                break  # -1 is returned if a character is not found
            check_subset += 1
        else:
            result.append(word)

    return result

def main():

    words = ['are', 'arrow', 'amore', 'aspire', 'assertive', 'arrogant', 'bartender', 'carter']
    are = ['a', 'r', 'e']
    ret = hasARE(words)
    print(f'The result is: {ret}')

    words = ['assertive', 'arrogant', 'bartender', 'carter', 'racer']
    are = ['a', 'r', 'e']
    ret = hasARE(words)
    print(f'The result is: {ret}')


if __name__ == '__main__':
    main()
