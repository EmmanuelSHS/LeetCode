#!/usr/bin/env python
# coding=utf-8

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        n = len(nums)
        sums = [ i for i in nums ]
        order = [i for i in range(n)]
        for i in range(1, n):
            sums[i] = sums[i - 1] + nums[i]
        
        order = [o for (s, o) in sorted( zip(sums, order) )]
        #print order
        sums.sort()
        #print sums

        start = 0
        end = 0
        diff = 1000000
        
        for i in range(1, n):
            tmp = abs(sums[i] - sums[i - 1])
            if tmp < diff:
                diff = tmp
                start = min(order[i - 1], order[i]) + 1
                end = max(order[i - 1], order[i])
        
        return [start, end]