#!/usr/bin/env python
# coding=utf-8

class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # need to record both local and global situation
        # global in maxn, local in minn
        n = len(nums)
        if n == 1:
            return nums[0]
        
        maxn = [ 0 for i in range(n + 1) ]
        minn = [0 for i in range(n + 1) ]
        res = nums[0]
        for i in range(1, n + 1):
            maxn[i] = nums[i - 1]
            minn[i] = nums[i - 1]
            if nums[i - 1] > 0:
                maxn[i] = max(maxn[i], maxn[i - 1]*nums[i - 1])
                minn[i] = min(minn[i], minn[i - 1]*nums[i - 1])
            elif nums[i - 1] < 0:
                maxn[i] = max(maxn[i], minn[i - 1]*nums[i - 1])
                minn[i] = min(minn[i], maxn[i - 1]*nums[i - 1])
            res = max(res, maxn[i])
            
        return res