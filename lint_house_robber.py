#!/usr/bin/env python
# coding=utf-8

class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            return A[0]
            
        f = [0 for i in range(n)]
        f[0] = A[0]
        f[1] = A[1]
        
        for i in range(2, n):
            f[i] = max(f[i - 1], f[i - 2] + A[i])
            
        return f[n - 1]