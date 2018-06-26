#!/usr/bin/env python3


def move_zeros(original_list):
    print('using remove and append (not push and pop :P )')
    count = len(original_list)
    for i in range(count):
        item = original_list[i]
        if item == 0:
            try:
                original_list.remove(item)
                original_list.append(item)
            except ValueError:
                pass
    return original_list


# def move_zeros2(original_list):
#     print('using remove and append (not push and pop :P )')
#     count = len(original_list)
#     non_zero_index = 0

#     for i in range(count):
#         item = original_list[i]
#         if item == 0 and i < count - 1:
#             try:
#                 next_item = 0
#                 while

#                 original_list[i] = original_list[i + 1]
#                 original_list[i + 1] = item

#                 for j in range(i + 1, count):
#                     item = original_list[j]
#                     if item == 0 and j < count - 1:
#                         original_list[j] = original_list[j + 1]
#                         original_list[j + 1] = item

#             except ValueError:
#                 pass
#     return original_list


if __name__ == '__main__':
    print(move_zeros([0, 1, 0, 3, 12]))
    # print(move_zeros2([0, 1, 0, 3, 12]))
    # print(move_zeros2([0, 1, 1, 0, 0, 3, 12, 0, 0]))
