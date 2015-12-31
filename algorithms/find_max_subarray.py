#!/usr/bin/env python
# coding=utf-8

NINF = -100000000000
def find_max_crossing_subarray(list, low, mid, high):
    left_sum = NINF
    sum = 0
    max_left = -1
    # reverse range need denote step = -1
    for i in range(mid, low - 1, -1):
        sum += list[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = NINF
    sum = 0
    max_right = -1
    for j in range(mid + 1, high + 1):
        sum += list[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum

def find_max_subarray(list, low, high):
    if low == high:
        return low, high, list[low]

    else:
        mid = (low + high) / 2
        left_low, left_high, left_sum = find_max_subarray(list, low, mid)
        right_low, right_high, right_sum = find_max_subarray(list, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(list, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

if __name__ == '__main__':
    '''
    finding the max sub array of this:
    a = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    equals to
    '''
    a = [0, 13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print len(a) - 1
    print find_max_subarray( a, 0, len(a)-1 )

