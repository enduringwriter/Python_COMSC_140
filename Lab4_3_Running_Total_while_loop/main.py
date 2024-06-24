def main():
    """
    This program calculates the running total of a list of numbers inputted by the user.
    Use a while loop.
    """
    total = 0

    while True:
        try:
            user_input = input("Enter a number (or 'q' to quit): ")
            if user_input == 'q':
                break
            total += int(user_input)
        except EOFError:
            print("EOFError encountered. Exiting.")
            break
    print(f"Total: {total}")

    return total

    # Walrus Operator
    # while True:
    #     try:
    #         if (user_input := input("Enter a number (or 'q' to quit): ")) != 'q':
    #             total += int(user_input)
    #         if user_input == 'q':
    #             break
    #     except EOFError:
    #         print("EOFError encountered. Exiting.")
    #         break
    # print(f"Total: {total}")
    # return total


    # Original code worked but it led to an EOFEerror
    # while (user_input := input("Enter a number (or 'q' to quit): ")) != 'q':
    #     total += int(user_input)
    # print(f'The total is {total}')
    # return total


if __name__ == '__main__':
    main()
