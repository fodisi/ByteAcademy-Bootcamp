# https: // www.hackerrank.com/challenges/30-2d-arrays/problem?h_r = next-challenge & h_v = zen

# Objective
# Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video!

# Context
# Given a  2D Array, :

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in to be a subset of values with indices falling in this pattern in 's graphical representation:

# a b c
#   d
# e f g
# There are  hourglasses in, and an hourglass sum is the sum of an hourglass' values.

# Task
# Calculate the hourglass sum for every hourglass in, then print the maximum hourglass sum.

# Input Format

# There are  lines of input, where each line contains  space-separated integers describing 2D Array
# every value in will be in the inclusive range of  to .

# Constraints

# Output Format

# Print the largest(maximum) hourglass sum found in .

# Sample Input

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output

# 19
# Explanation

#  contains the following hourglasses:

# 1 1 1   1 1 0   1 0 0   0 0 0
#   1       0       0       0
# 1 1 1   1 1 0   1 0 0   0 0 0

# 0 1 0   1 0 0   0 0 0   0 0 0
#   1       1       0       0
# 0 0 2   0 2 4   2 4 4   4 4 0

# 1 1 1   1 1 0   1 0 0   0 0 0
#   0       2       4       4
# 0 0 0   0 0 2   0 2 0   2 0 0

# 0 0 2   0 2 4   2 4 4   4 4 0
#   0       0       2       0
# 0 0 1   0 1 2   1 2 4   2 4 0
# The hourglass with the maximum sum() is:

# 2 4 4
#   2
# 1 2 4


#!/bin/python3

import math
import os
import random
import re
import sys


def create_matrix():
    # return [[0, 1, 2, 0, 3, 0],
    #         [1, 3, 2, 0, 3, 0],
    #         [2, 1, 2, 0, 3, 0],
    #         [3, 1, 2, 0, 3, 0],
    #         [4, 1, 2, 0, 3, 0],
    #         [5, 1, 2, 0, 3, 0]]
    # return [[0, 1, 2, 3],
    #         [2, 3, 4, 5],
    #         [3, 4, 5, 6],
    #         [4, 5, 6, 7]]

    return [[0, -1, -2, -3],
            [-2, -3, -4, -5],
            [-3, -4, -5, -6],
            [-4, -5, -6, -7]]


def create_hourglass(matrix, start_row, start_col):
    hourglass = []
    hourglass.append(matrix[start_row][start_col:start_col + 3])
    hourglass.append([matrix[start_row + 1][start_col + 1]])
    hourglass.append(matrix[start_row + 2][start_col:start_col + 3])
    return hourglass


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # arr = create_matrix()
    hourglasses = []
    for row in range(len(arr) - 2):
        for col in range(len(arr) - 2):
            h = create_hourglass(arr, row, col)
            # print(h)
            hourglasses.append(h)
    # print(hourglasses)

    max_ = 0
    for i in range(len(hourglasses)):
        item = hourglasses[i]
        sum_ = 0
        # print(item)
        for j in range(len(item)):
            sum_ += sum(item[j])
        # print(sum_)

        if i == 0:
            max_ = sum_

        if sum_ > max_:
            max_ = sum_

    print(max_)
