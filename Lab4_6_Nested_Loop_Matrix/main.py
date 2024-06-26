def main():
    """
    This program is designed to print the pairs of indices for the lower left half of an N x N matrix.
    The lower left half includes the diagonal and all elements below it. The program uses nested loops to achieve this.
    The program also prints the total number of iterations.
    N is provided by the user.
    """
    
    iternum = 0
    N = int(input('Welcome of the matrix. Enter the dimension of N: '))

    for i in range(N):
        for j in range(i, N):
            print(f'({i}, {j})', end=' ')
            iternum += 1
    print(f'\nTotal iterations: {iternum}')

    return iternum


if __name__ == '__main__':
    main()