def main():
    """
    Identify the Quadrant Number for x,y Coordinates
    """

    x = int(input('Enter x-coordinate: '))
    y = int(input('Enter y-coordinate: '))

    if x > 0 and y > 0:
        quadrant = 1
    elif x < 0 and y > 0:
        quadrant = 2
    elif x < 0 and y < 0:
        quadrant = 3
    elif x > 0 and y < 0:
        quadrant = 4
    elif x == 0 and y == 0:
        quadrant = 'Origin'
    elif x == 0:
        quadrant = 'Y-axis'
    else:  # y == 0
        quadrant = 'X-axis'

    print(f'Coordinates (x,y): ({x},{y}).    Quadrant: {quadrant}.')
    ########################################
    # Do not delete the return statement
    ########################################
    return quadrant


if __name__ == '__main__':
    main()
