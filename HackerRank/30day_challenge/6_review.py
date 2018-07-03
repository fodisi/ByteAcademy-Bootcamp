# Objective
# Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given a string, , of length  that is indexed from to, print its even-indexed and odd-indexed characters as space-separated strings on a single line(see the Sample below for more detail).

# Note: is considered to be an even index.

# Input Format

# The first line contains an integer,  (the number of test cases).
# Each line  of the  subsequent lines contain a String, .

# Constraints

# Output Format

# For each String(where), print 's even-indexed characters, followed by a space, followed by 's odd-indexed characters.

# Sample Input

# 2
# Hacker
# Rank
# Sample Output

# Hce akr
# Rn ak
# Explanation

# Test Case 0:


# The even indices are, , and, and the odd indices are, , and . We then print a single line of  space-separated strings
# the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices().

# Test Case 1:


# The even indices are and, and the odd indices are and . We then print a single line of space-separated strings
# the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices().


#!/usr/bin/env python3


if __name__ == '__main__':
    N = int(input())
    lines = []
    for _ in range(N):
        lines.append(input())

    for line in lines:
        even_chars, odd_chars = [], []
        for i in range(len(line)):
            if i % 2 == 0:
                even_chars.append(line[i])
            else:
                odd_chars.append(line[i])

        print('{0} {1}'.format(''.join(even_chars),
                               ''.join(odd_chars)))
