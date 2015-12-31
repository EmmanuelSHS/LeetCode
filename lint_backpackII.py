#!/usr/bin/env python
# coding=utf-8

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A & V: Given n items with size A[i] and value V[i]
    @return: The maximum value
    """

    """
    DP solution:
        1. define a optimal global & its optimal subproblem: value at i-th item with size j.
        2. decide how this optimal is formed
    """
    def backPackII(self, m, A, V):
        n = len(A)
        value = [[0 for i in range(0, m)] for j in range(0, n )]
        for i in range(0, n):
            for j in range(0, m):
                value[i][j] = max(value[i-1][j], value[i-1][j-A[i]] + V[i]) if A[i] < j else value[i-1][j]
        return value[n][m]

s = Solution()
print s.backPackII(10, [2, 3, 5, 7], [1, 5, 2, 4,])
