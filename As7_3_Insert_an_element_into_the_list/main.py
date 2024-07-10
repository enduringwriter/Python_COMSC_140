"""
This program inserts an integer value into a sorted list, maintaining the sorted order.
Do not use sort or sorted functions.

Assumptions: Input list is already sorted.
"""


def insertOne(numbers, val):
    for i in range(len(numbers)):
        if val < numbers[i]:
            numbers.insert(i, val)
            break
        if val > max(numbers):
            numbers.append(val)
            break

    # alternative solution
    # for i, n in enumerate(numbers):
    #     if val < n:
    #         numbers.insert(i, val)
    #         break
    #     if val > max(numbers):
    #         numbers.append(val)
    #         break
    # # else:
    # #     numbers.append(val)

def main():
    numbers = [5, 20, 30, 35, 50]
    print(f'The original list value: {numbers}')
    insertOne(numbers, 25)
    print(f'After insertion 25: {numbers}')


if __name__ == '__main__':
    main()
