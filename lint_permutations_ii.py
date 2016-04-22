#!/usr/bin/env python
# coding=utf-8

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    key is deep copy shallow copy
    """
    def permuteUnique(self, nums):
        # write your code here
        if not nums:
            return []
        n = len(nums)
        if n == 1:
            return nums
        res = [[nums[0]]]
        
        for i in range(1, n):
            nr = len(res)
            np = len(res[0])
            for j in range(nr):
                tmp = res[j][:]
                for k in range(np + 1):
                    tmp.insert(k, nums[i])
                    if tmp not in res:
                        res.append(tmp[:])
                    tmp.pop(k)
            res = res[nr:]
            
        return res