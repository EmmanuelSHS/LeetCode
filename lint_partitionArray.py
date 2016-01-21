#!/usr/bin/env python
# coding=utf-8

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    O(n) runtime
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        p = 0

        for x in nums:
            if x < k:
                p += 1
        
        return p

if __name__ == '__main__':
    s = Solution()
    input = [3,2,2,1]; k = 2
    input = [9,9,9,8,9,8,7,9,8,8,8,9,8,9,8,8,6,9]; k = 9
    input = [1,2,2,2]; k = 3
    print s.partitionArray(input, k)
