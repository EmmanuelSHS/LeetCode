#!/usr/bin/env python
# coding=utf-8

class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    #key is that some number sits on the boundary
    def findPeak(self, A):
        # write your code here
        n = len(A)
        
        start = 0
        end = n - 1
        while start <= end:
            mid = (start + end) / 2
            left = A[mid - 1]
            right = A[mid + 1]
            if left < A[mid] and right < A[mid]:
                return mid
            elif left > A[mid] and right < A[mid]:
                end = mid - 1
            else:
                start = mid + 1

        
