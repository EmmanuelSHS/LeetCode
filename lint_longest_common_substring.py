#!/usr/bin/env python
# coding=utf-8

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        A = A[:]
        B = B[:]
        n = len(A)
        m = len(B)
        
        f = [ [0 for i in range(m + 1)] for j in range(n + 1) ]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i-1] == B[j-1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = 0
                
        res = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if f[i][j] > res:
                    res = f[i][j]
                    
        return res