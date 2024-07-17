"""
This program splits the list values based on the pivot value,
which is the last element of the list.
Numbers less than the pivot are on the left, the pivot is in the middle,
and numbers greater than the pivor are on the right.
"""

def split(number):
    pivot = number[-1]

    left, right = [], []
    for n in number[:-1]:
        if n < pivot:
            left.append(n)
        else:
            right.append(n)
    number = left + [pivot] + right
    return number

def main():
    # number = list(map(int, input().split()))
    number = [35, 5, 10, 20, 40, 15]
    number = split(number)
    print(number)


if __name__ == '__main__':
    main()
