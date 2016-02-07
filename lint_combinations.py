#!/usr/bin/env python
# coding=utf-8

class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    key point is to copy value
    """
    def combine(self, n, k):      
        # write your code here  
        res = []
        tmp = []
        self.combineK(n, k, 1, tmp, res)
        
        return res
        
    def combineK(self, n, k, start, tmp, res):
        if k == 0:
            res.append(tmp[:])
        
        for i in range(start, n + 1):
            tmp.append(i)
            self.combineK(n, k - 1, i + 1, tmp, res)
            tmp.pop()