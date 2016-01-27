#!/usr/bin/env python
# coding=utf-8

import copy
class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0])
        
        f = copy.deepcopy(grid)
        for i in range(1, n):
            f[0][i] = f[0][i - 1] + grid[0][i]
        for i in range(1, m):
            f[i][0] = f[i - 1][0] + grid[i][0]
            
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = min(f[i - 1][j], f[i][j - 1]) + grid[i][j]
                
        return f[m-1][n-1]
        
        
