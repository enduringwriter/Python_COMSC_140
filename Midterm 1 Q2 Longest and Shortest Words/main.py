def main():
    """
    Midterm 1. Question 2.
    This program takes multiple string inputs from the user and returns the longest and shortest
    words in the string. If there are multiple, the first instance is returned.
    The program ends when the user enters, 'stop' or 'STOP'.
    """
    
    longest = ""
    shortest = "a" * 10000
    
    while True:
        word = input("Enter a word or 'stop' to quit: ").lower()
        if word == 'stop':
            break
        else:
            if len(word) > len(longest):
                longest = word
            if len(word) < len(shortest):
                shortest = word
                
    print(f"The longest word is: {longest}")
    print(f"The shortest word is: {shortest}")
    
    return longest, shortest

if __name__ == '__main__':
    main()
