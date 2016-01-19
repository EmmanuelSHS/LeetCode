#!/usr/bin/env python
# coding=utf-8

class Solution:
    '''
    @para k & A, input array A, k-th largest
    @para return ans an integer
    O(n) running time, O(1) extra space
    '''
    def kthLargestElement(self, k, A):
        return self.rselect(A, 0, len(A) - 1, k)
    
    def swap(self, A, x, y):
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp
        
    def rpartition(self, A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] > x:
                i += 1
                self.swap(A, i, j)
        self.swap(A, i+1, r)
        return i + 1
    
    def rselect(self, A, p, r, i):
        if p == i:
            return A[p]
        q = self.rpartition(A, p, r)
        k = q - p + 1
        if k == i:
            return A[q]
        elif k < i:
            return self.rselect(A, q+1, r, i-k)
        elif k > i:
            return self.rselect(A, p, q-1, i)

