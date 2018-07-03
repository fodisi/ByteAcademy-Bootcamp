# https://www.hackerrank.com/challenges/30-sorting/problem


#!/usr/bin/env python3


def bubble_sort(list_):
    # Track total number of elements swapped during the ordering process
    totalSwaps = 0
    lenght = len(list_)

    for _ in range(lenght):
        # Track number of elements swapped during a single array traversal
        swaps = 0

        for j in range(lenght-1):
            # Swap adjacent elements if they are in decreasing order
            if list_[j] > list_[j+1]:
                tmp = list_[j]
                list_[j] = list_[j+1]
                list_[j+1] = tmp
                swaps += 1

        # Updates the total of swaps performed so far.
        totalSwaps += swaps

        # If no elements were swapped during a traversal, array is sorted
        if swaps == 0:
            break

    return list_, totalSwaps


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    # Write Your Code Here
    order_list, swaps = bubble_sort(a)
    if len(order_list) > 0:
        print('Array is sorted in {0} swaps.'.format(swaps))
        print('First Element: {}'.format(order_list[0]))
        print('Last Element: {}'.format(order_list[len(order_list)-1]))
