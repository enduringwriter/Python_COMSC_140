def main():
    """
    The program generates a sequence of numbers where each number is the sum of the previous two numbers.
    The user provides two initial integers and the total number of values (N) in the sequence (where N > 2).
    The resulting sequence is stored in a list named "result".
    The program outputs all values in this sequence based on the user's input.

    Assumptions: initial integer inputs >= 1
    """

    result = []
    while True:
        try:
            a1 = int(input('Enter your first number: '))
            a2 = int(input('Enter your second number: '))
            N = int(input('Enter the number of sequences: '))
        except ValueError:
            print('Please enter a valid entry.')
        else:
            if a1 >= 1 and a2 >=1 and N > 2:
                result.extend([a1, a2])
                for _ in range(N-2):
                    result.append(result[-1] + result[-2])
                break
            else:
                print('Please ensure the initial numbers are >= 1 and N > 2.')
    
    print(*result)

    return result


if __name__ == '__main__':
    main()
