#!/usr/bin/env python
# coding=utf-8

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        if len(s) == 1:
            return [[s]]
        res = []
        tmp = []
        self.findPali(s, 0, res, tmp)
        return res
        
    def findPali(self, s, start, res, tmp):
        if start == len(s):
            res.append(tmp[:])
            return
        
        for i in range(start, len(s)):
            if self.isPali(s, start, i):
                tmp.append(s[start:i+1])
                self.findPali(s, i+1, res, tmp)
                tmp.pop()
        
    def isPali(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
            