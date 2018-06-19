# Manasa loves the nim game, in which there are  buckets, each having  balls. Two players play alternately. Each turn consists of removing some non-zero number of balls from one of the bucket. A player with lack of moves looses. But, Manasa having played it so many times, she gets bored one day. So she wants to change the rules of the game. She loves prime numbers, so she makes a new rule: any player can only remove a prime number of balls from a bucket. But there are infinite number prime numbers. So to keep the game simple, a player can only remove  balls from a bucket if belongs to the set

# The whole game can now be described as follows:

# There are  buckets, and the  bucket contains  balls. A player can choose a bucket and remove  balls from that bucket where  belongs to . A player loses if there are no more available moves.

# Manasa plays the first move against Sandy. Who will win if both of them play optimally?

# Input Format

# The first line contains an integer, the number of test cases.

# Each test case consists of two lines. The first line contains a single integer . The second line contain  space-separated integers .

# Constraints

# Output Format

# Print a single line containing the name of the winner: Manasa or Sandy.

# Sample Input 0

# 2
# 2
# 10 10
# 3
# 2 2 3
# Sample Output 0

# Sandy
# Manasa
# Explanation 0

# For the first testcase: Since both the buckets have same number of balls, Manasa can choose any one of them for her first move. If Manasa selects to remove or balls to remove from first bucket. Now, Sandy can always counter her move by removing  balls from first bucket if it's left with balls respectively. Now, there are no valid moves left for first bucket. The same thing repeats for second bucket and Sandy wins.

# For the second testcase: Manasa removes  balls from the third bucket. Now, if Sandy choose the remove  balls from second bucket Manasa will empty the first bucket and if Sandy choose the remove  balls from first bucket, Manasa will empty second one. Hence, Manasa wins.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the winner function below.


def winner(A):
    # Return the name of the winner of the game


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = winner(A)

        fptr.write(result + '\n')

    fptr.close()
