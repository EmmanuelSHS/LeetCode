#!/usr/bin/env python
# coding=utf-8

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        n = len(A)
        f = [False for i in range(n)]
        f[0] = True
        
        for i in range(n):
            for j in range(i):
                tmp = f[j] and ( (i-j) <= A[j] )
                f[i] = f[i] or tmp
                
        return f[n - 1]
    '''
    solution ii, copyright by 'JustForWanShua' From leetcode

    class Solution(object):
        def canJump(self, nums):
            maxEdge = 0
            for i in range(len(nums)):
                if maxEdge < i:
                    return False
                maxEdge = max(maxEdge, i+nums[i])
        return True

    '''
