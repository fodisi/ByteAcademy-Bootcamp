# Concatenate
#
# Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:
#
# import numpy
#
# array_1 = numpy.array([1,2,3])
# array_2 = numpy.array([4,5,6])
# array_3 = numpy.array([7,8,9])
#
# print numpy.concatenate((array_1, array_2, array_3))
#
# #Output
# [1 2 3 4 5 6 7 8 9]
# If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.
#
# import numpy
#
# array_1 = numpy.array([[1,2,3],[0,0,0]])
# array_2 = numpy.array([[0,0,0],[7,8,9]])
#
# print numpy.concatenate((array_1, array_2), axis = 1)
#
# #Output
# [[1 2 3 0 0 0]
#  [0 0 0 7 8 9]]
# Task
#
# You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .
#
# Input Format
#
# The first line contains space separated integers ,  and .
# The next  lines contains the space separated elements of the  columns.
# After that, the next  lines contains the space separated elements of the  columns.
#
# Output Format
#
# Print the concatenated array of size X.
#
# Sample Input
#
# 4 3 2
# 1 2
# 1 2
# 1 2
# 1 2
# 3 4
# 3 4
# 3 4
# Sample Output
#
# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]]

import numpy as np

if __name__ == '__main__':
    values = [int(x) for x in input().split(' ')]
    rows_1 = values[0]
    rows_2 = values[1]
    cols = values[2]

    array_1 = []
    array_2 = []

    for _ in range(rows_1):
        array_1.append([int(c) for c in input().split(' ')])

    for _ in range(rows_2):
        array_2.append([int(c) for c in input().split(' ')])

    np_array_1 = np.array(array_1)
    np_array_2 = np.array(array_2)

    # print(np_array_1)
    # print(np_array_2)

    print(np.concatenate((np_array_1, np_array_2), 0))





