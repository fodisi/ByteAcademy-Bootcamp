#import numpy as np
#A=testmatrix.txt
#row_sum = np.sum(A, axis=0)#---
#col_sum = np.sum(A, axis=1)#|||

#row_sum.sort(reberse=True)
## I have to sort all the columns according to this result ,but I cannot find the way


#col_sum.sort(reberse=True)
##also


from operator import itemgetter


def get_matrix():
    #matrix = [
    #    [13, 14, 15, 16],
    #    [9, 10, 11, 12],
    #    [5, 6, 7, 8],
    #    [1, 2, 3, 4],
    #]

    matrix = [
        [10, 5, 4, 20],
        [9, 33, 27, 16],
        [11, 6, 55, 3],
    ]
    
    print("Load matrix from:")
    print("1 - File")
    print("Other key - Hard coded")
    if input() == "1":
        matrix = get_matrix_from_file()
    return matrix


#Reads a file and returns a matrix [[0],[],..,[n]]
def get_matrix_from_file():
    matrix = []
    with open("textmatrix.txt", "r") as file:
        for line in file:
            str_values = line.rstrip('\n').split()
            if len(str_values) > 0:
                matrix.append(([int(i) for i in str_values]))
    return matrix


#Returns a list of tuples with index and sum of each row in a matrix,
#sorted by sum in descending order.
def get_sorted_rows_sum(matrix):
    result = {}
    row_count = len(matrix)
    for row_index in range(row_count):
        result[row_index] = sum(matrix[row_index])
    return sorted(result.items(), key=itemgetter(1))


#Returns a list of tuples with index and sum of each column in a matrix,
#sorted by sum in descending order.
def get_sorted_columns_sum(matrix):
    result = {}
    col_count = len(matrix[0])
    for col_index in range(col_count):
        result[col_index] = sum([row[col_index] for row in matrix])
    return sorted(result.items(), key=itemgetter(1))


def get_row_sorted_matrix(rows_sum_index, matrix):
    sorted_matrix = []
    for cur_index, cur_sum in rows_sum_index:
        sorted_matrix.append(matrix[cur_index])
    return sorted_matrix


def get_col_sorted_matrix(cols_sum_index, matrix):
    sorted_matrix = []
    for row in matrix:
        sorted_row = []
        for cur_index, cur_sum in cols_sum_index:
            sorted_row.append(row[cur_index])
        sorted_matrix.append(sorted_row)
    return sorted_matrix

def print_matrix(matrix):
    #nested list comprehension code would be:
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    #  for row in col_sorted_matrix]))

    for row in matrix:
        print(''.join(['| {:4}'.format(str(col).zfill(3)) for col in row]),
              end='|\n')


if __name__ == '__main__':
    #Gets the base matrix
    matrix = get_matrix()
    
    #Gets a list[(index, sum)] containing the sum of each row/col, and the index each row/col in relation to the original matrix.
    #The returned list will be sorted in ascending order by the sum of the row/col.
    row_sum_list = get_sorted_rows_sum(matrix)
    col_sum_list = get_sorted_columns_sum(matrix)
    
    #created matrices sorted by sum of rows and cols
    row_sorted_matrix = get_row_sorted_matrix(row_sum_list, matrix)
    col_sorted_matrix = get_col_sorted_matrix(col_sum_list, matrix)
    
    #Prints data
    print('Row sum and indexes')
    print(row_sum_list)
    print('Col sum and indexes')
    print(col_sum_list)
    print()
    print('Original matrix')
    print_matrix(matrix)
    print()
    print('Matrix with ROWS sorted by their sums')
    print_matrix(row_sorted_matrix)
    print()
    print('Matrix with COLS sorted by their sums')
    print_matrix(col_sorted_matrix)
#END

