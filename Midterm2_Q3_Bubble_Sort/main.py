"""
This program sorts a list of numbers by swapping adjacent numbers,
if the number on the left is greater than the number on the right.

Did not finish this program.
"""


def bubblesort(number):
    for i in range(len(number)-1):
        if number[i] > number[i + 1]:
            number[i], number[i + 1] = number[i + 1], number[i]
    return number

def bubble(number):
    for _ in range(len(number)):
        yield bubblesort(number)

def main():
    number = list(map(int, input().split()))
    bubblesort(number)
    print(number)


if __name__ == '__main__':
    main()
