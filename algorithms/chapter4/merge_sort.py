#!/usr/bin/env python
# coding=utf-8

def mergeSort(nums):
    n = len(nums)
    if n == 1:
        return nums

    left = nums[:n/2]
    right = nums[n/2:]

    res = []
    p1, p2 = 0, 0

    while p1 < n / 2 and p2 < n / 2:
        if left[p1] <= right[p2]:
            res.append(left[p1])
            p1 += 1
        else:
            res.append(right[p2])
            p2 += 1

    res = res + left[p1:] if p1 < n / 2 else res + right[p2:]

    return res


if __name__ == '__main__':
    test = [2, 5, 4, 6, 7]
    print mergeSort(test)
