# https: // www.hackerrank.com/challenges/30-binary-numbers/problem

# Objective
# Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given a base - integer, , convert it to binary(base-). Then find and print the base - integer denoting the maximum number of consecutive 's in 's binary representation.

# Input Format

# A single integer, .

# Constraints

# Output Format

# Print a single base - integer denoting the maximum number of consecutive 's in the binary representation of .

# Sample Input 1

# 5
# Sample Output 1

# 1
# Sample Input 2

# 13
# Sample Output 2

# 2
# Explanation

# Sample Case 1:
# The binary representation of is, so the maximum number of consecutive 's is .

# Sample Case 2:
# The binary representation of is, so the maximum number of consecutive 's is .


#!/bin/python3


import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    binary = "{0:b}".format(n)
    consecutives = 0
    aux = 0
    for digit in binary:
        if digit == '1':
            aux += 1
        else:
            aux = 0

        if aux > consecutives:
            consecutives = aux

    print(consecutives)
