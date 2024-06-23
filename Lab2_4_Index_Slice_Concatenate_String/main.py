def main():
    """
    Apply indexing and slicing, and concatenation on a string.
    """

    original_str = 'Python Programming'
    
    sub1 = original_str[:6]
    sub2 = original_str[7:]
    merged_str = sub2 + " " + sub1

    print(sub2)
    print(sub1)
    print(merged_str)

    return sub1, sub2, merged_str


if __name__ == '__main__':
    main()
