#!/usr/bin/env python
# coding=utf-8

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    Key point is that stop condition could be embedded in for loop
    """
    def subsets(self, S):
        # write your code here
        n = len(S)
        if n == 0:
            return [[]]
        if n == 1:
            return [[], S]
        res = [[]]
        tmp = []
        S.sort()
        self.allSub(S, res, tmp, 0, n)
        return res
    
    def allSub(self, S, res, tmp, start, end):
        for i in range(start, end):
            tmp.append(S[i])
            res.append(tmp[:])
            if i < end - 1:
                self.allSub(S, res, tmp, i + 1, end)
            tmp.pop()
            
            