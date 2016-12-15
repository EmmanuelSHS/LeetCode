#!/usr/bin/env python
# coding=utf-8

class Solution:
    def pawnLen(self, nums):
        '''
        quick & slow ptr
        by meet with each other, slow ptr has walked a pawnLen
        '''
        n = len(nums)

        p1 = nums[0]
        p2 = nums[nums[0]]
        c1 = 1
        while p1 != p2:
            c1 += 1
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 >= n or p2 >= n:
                return 0

        return c1


if __name__ == '__main__':
    s = Solution()
    print s.pawnLen([2, 3, 1, 1, 3])
    print s.pawnLen([1,2,3,4,1])
    print s.pawnLen([1,2,3,4])
