# https://www.hackerrank.com/challenges/30-linked-list/problem


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method
        if head == None:
            return Node(data)
        head.next = self.insert(head.next, data)
        return head


if __name__ == '__main__':
    mylist = Solution()
    T = int(input())
    head = None
    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)
    mylist.display(head)
