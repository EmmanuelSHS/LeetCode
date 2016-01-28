#!/usr/bin/env python
# coding=utf-8

class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        # write your code here
        if n == 0:
            return 1
        f = [0 for i in range(n + 1)]
        f[0] = 1
        f[1] = 1
        
        for i in range(2, n+1):
            for j in range(i):
                f[i] += f[j]*f[i-j-1]
                
        return f[n]