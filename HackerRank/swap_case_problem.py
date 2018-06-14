# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#
# For Example:
#
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
# Input Format
#
# A single line containing a string .
#
# Constraints
#
#
# Output Format
#
# Print the modified string .
#
# Sample Input 0
#
# HackerRank.com presents "Pythonist 2".
# Sample Output 0
#
# hACKERrANK.COM PRESENTS "pYTHONIST 2".


def swap_case(s):
    new_str = []
    for ch in s:
        if ch.isalpha() and ch.islower():
            new_str.append(ch.upper())
        elif ch.isalpha() and ch.isupper():
            new_str.append(ch.lower())
        else:
            new_str.append(ch)

    return ''.join(new_str)


if __name__ == '__main__':
    print(swap_case('HackerRank.com presents "Pythonist 2"'))