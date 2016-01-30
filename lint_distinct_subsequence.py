#!/usr/bin/env python
# coding=utf-8

class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # DP since compared T[i+1] to S requires previous knowledge on counting T[i]
        S = S[:]
        T = T[:]
        n = len(S)
        m = len(T)
        
        if n == 0 or m == 0:
            return 1
        f = [ [0 for i in range(m + 1)] for j in range(n + 1) ]
                
        for i in range(n+1):
                f[i][0] = 1
                
        for i in range(1, n+1):
            for j in range(1, m+1):
                if S[i-1] == T[j-1]:
                    f[i][j] = f[i-1][j-1] + f[i-1][j]
                else:
                    f[i][j] = f[i-1][j]
                
        return f[n][m]
        