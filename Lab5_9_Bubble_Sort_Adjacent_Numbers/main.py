import random
"""
This program sorts a list of numbers by swaping adjacent numbers,
if the number on the left is greater than the number on the rigt.
This results in the largest number moving to the end of the list.
"""

def bubble(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        else:
            continue

def main():
    numbers = [2, 3, 0, 5, 4]
    print(numbers)
    bubble(numbers)
    print(numbers)    # must be [2, 0, 3, 4, 5]

    numbers = [random.randint(0, 10) for i in range(10)]
    print(numbers)
    bubble(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
