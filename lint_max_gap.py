#!/usr/bin/env python
# coding=utf-8

class Solution:
     # @param nums: a list of integers
     # @return: the maximum difference
    def maximumGap(self, nums):
        # write your code here
        if len(nums) == 1:
            return 0
        
        n = 5
        size = max(nums) / n
        if size == 0:
            size = len(nums)
            
        bins = [[] for i in range(n + 1)]
        
        for x in nums:
            bins[x/size].append(x)

        for bin in bins:
            bin.sort()
            list.extend(bin)
        res = 0
        for i in range(1, len(list)):
            tmp = list[i] - list[i - 1]
            if tmp > res:
                res = tmp
        return res

if __name__ == '__main__':
    s = Solution()
    input = [3,2,1,4,3]
    print s.maximumGap(input)
