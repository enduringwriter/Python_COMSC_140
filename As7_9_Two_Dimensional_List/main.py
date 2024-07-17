def getMaxElement(numbers):
    """
    This program conducts operations on two-dimensional lists,
    e.g. finding the maximum element in the entire list of lists and the maximum value of each row,
    and calculating the sum of each row and the sum of each column.
    
    Assumptions: None.
    """
    
    print(f'2D Array: {numbers}')

    number_of_rows = len(numbers)
    print(f'Number of rows: {number_of_rows}')

    number_of_elements_per_row = [len(r) for r in numbers]
    print(f'Number of elements per row: {number_of_elements_per_row}')
    
    total_columns = max([len(r) for r in numbers])
    print(f'Nunmber of columns: {total_columns}')
    
    temp_max, max_number = 0, 0
    for r in range(len(numbers)):
        temp_max = max(numbers[r])
        if temp_max > max_number:
            max_number = temp_max
    return max_number


def getSumRows(numbers):
    
    # old method
    # sum_row, 
    # for r in range(len(numbers)):
    #     for i in numbers[r]:
    #         sum_row += i
    #     sum_rows.append(sum_row)
    
    sum_rows = []
    for row in numbers:
        sum_row = sum(row)
        sum_rows.append(sum_row)
    return sum_rows


def getSumCols(numbers):
    
    total_columns = max([len(row) for row in numbers])
    sum_cols = [0] * total_columns
    for row in numbers:
        for i in range(len(row)):
            sum_cols[i] += row[i]
    return sum_cols


def getMaxElmRow(numbers):
    max_in_row = 0
    max_in_row_list = []
    for row in numbers:
        max_in_row = max(row)
        max_in_row_list.append(max_in_row)
    return max_in_row_list


def main():
    ##################################################
    numbers = [[99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24, 56],
               [33, 77, 32, 33, 34]]
    ##################################################
    ret = getMaxElement(numbers)
    print('Return value from getMaxElement', ret)

    ret = getSumRows(numbers)
    print('Return value from getSumRows', ret)

    ret = getSumCols(numbers)
    print('Return value from getSumCols', ret)

    ret = getMaxElmRow(numbers)
    print('Return value from getMaxElmRow', ret)


if __name__ == '__main__':
    main()
