# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.

# Constraints

# Output Format

# Print the runner-up score.

# Sample Input 0

# 5
# 2 3 6 6 5
# Sample Output 0

# 5
# Explanation 0

# Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.

def runner_up():
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort(reverse = True)
    print(next((i for i in arr if i < arr[0]), arr[0]))

runner_up()