#!/usr/bin/env python
# coding=utf-8

import sys


class Solution:
    def maxNumber(self, nums1, nums2, k):
        # Write your code here
        m, n = len(nums1), len(nums2)

        # max(nums1, nums2) returns the list the first of which is max
        nums = [ max(nums1, nums2).pop(0) for _ in nums1 + nums2 ]
        
        print n, m
        
        if m + n == k:
            return nums
        
        for i in range(n + m - k):
            p = -1
            m = sys.maxint
            for j, x in enumerate(nums):
                if x < m:
                    p = j
                    m = x
            nums.pop(p)
        
        return nums

if __name__ == '__main__':
    nums1 = [3,4,6,5]
    nums2 = [9,1,2,5,8,3]
    k = 5
    s = Solution()
    print s.maxNumber(nums1, nums2, k)
