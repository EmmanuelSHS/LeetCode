#!/usr/bin/env python
# coding=utf-8

'''
many base cases
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        n = len(A)
        i = 0
        step = 0

        while ( i < n):
            l = i + A[i]
            step += 1
            if l > n:
                return step
            tmp = l
            for j in range(i, l + 1):
                if j + A[j] > l and j + A[j] > tmp:
                    tmp = j + A[j]
            i = l if tmp < l else tmp
        return step
            
