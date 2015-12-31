#!/usr/bin/env python
# coding=utf-8

class Solution:

    def median(self, nums):
        maxn = max(nums)
        minn = min(nums)
        mindex = len(nums)/2 if len(nums)%2 == 0 else len(nums)/2 + 1
        
        res = [0 for i in range(minn, maxn+1)]

        for x in nums:
            res[x - minn] += 1
        
        for i in range(len(res)):
            mindex -= res[i]
            if mindex <= 0:
                return i + minn
            
if __name__ == '__main__':
    s = Solution()
    print s.median([4,5,1,3,2])
    print s.median([4,5,7,9])
