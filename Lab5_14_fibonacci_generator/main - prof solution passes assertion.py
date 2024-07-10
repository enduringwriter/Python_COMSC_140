def fibo(N):
    """
    Use the `yield` statement to create a generator that generates the first N elements of the Fibonacci sequence.
    Generators are ideal for conserving memory when working with large datasets or data streams.
    """

    # current, next = 0, 1
    # for _ in range(N):
    #     yield current
    #     current, next = next, current + next

    #### Solution 1
    xn2 = 0
    xn1 = 1
    i = 0
    while i <= N:
        yield xn2
        # tmp = xn2
        # xn2 = xn1
        # xn1 = xn1 + tmp
        xn2, xn1 = xn1, xn1 + xn2
        i += 1
        

def main():
    N = 16
    gen = fibo(N)
    # for v in gen:
    #     print(v, end=' ')
    print(list(gen))


if __name__ == '__main__':
    main()
