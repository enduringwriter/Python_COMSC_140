import math

def isPrime(num):
    if num < 2:
        return False
    numbers_to_divide = int(math.sqrt(num))
    for i in range(2, numbers_to_divide + 1):  # include the last number in the range
        if num % i == 0:
            return False  # number is not a prime number
    else:
        return True  # number is a prime number


def primeNumbers(begin, end):  
    plist = []
    for number in range(begin, end + 1):  # include 'end' in the range
        if isPrime(number):
            plist.append(number)
    return plist


def main():
    begin = 0
    end = 20
    rlst = primeNumbers(begin, end)
    print(rlst)

    begin = 10
    end = 50
    rlst = primeNumbers(begin, end)
    print(rlst)


if __name__ == '__main__':
    main()
