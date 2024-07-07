
def consonant(strval):
    """
    Lab5_15_consonant_generator_using_yield

    Create a generator function that yields all consonants from a given string,
    filtering out vowels and non-alphabet characters.
    """

    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']    

    for l in strval:
        if l not in vowels and l.isalpha():
            yield l


def main():
    strval = 'Python Programming'
    mygen = consonant(strval)
    
    rlst = list(mygen)
    print(len(rlst))
    for v in rlst:
        print(v, end=' ')
    print()


if __name__ == '__main__':
    main()
