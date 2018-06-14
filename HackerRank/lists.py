# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
#
# Input Format
#
# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.
#
# Constraints
#
# The elements added to the list must be integers.
# Output Format
#
# For each command of type print, print the list on a new line.
#
# Sample Input 0
#
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0
#
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

def init_commands():
    list_ = []
    list_.append('insert 0 5'.split(' '))
    list_.append('insert 1 10'.split(' '))
    list_.append('insert 0 6'.split(' '))
    list_.append('print'.split(' '))
    list_.append('remove 6'.split(' '))
    list_.append('append 9'.split(' '))
    list_.append('append 1'.split(' '))
    list_.append('sort'.split(' '))
    list_.append('print'.split(' '))
    list_.append('pop'.split(' '))
    list_.append('reverse'.split(' '))
    list_.append('print'.split(' '))
    return list_




if __name__ == '__main__':
    #N = int(raw_input())
    N = int(input())
    #print(N)
    commands = []
    #commands = init_commands()

    my_list = []
    for i in range(N):
        commands.append(input().split(' '))

    for item in commands:
        cmd = item[0]
        if cmd == 'insert':
            index = int(item[1])
            element = int(item[2])
            my_list.insert(index, element)
        elif cmd == 'print':
            print(my_list)
        elif cmd == 'remove':
            my_list.remove(int(item[1]))
        elif cmd == 'append':
            my_list.append(int(item[1]))
        elif cmd == 'sort':
            my_list.sort()
        elif cmd == 'pop':
            my_list.pop()
        elif cmd == 'reverse':
            my_list.reverse()




















