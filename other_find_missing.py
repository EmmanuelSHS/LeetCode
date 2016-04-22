#!/usr/bin/env python
# coding=utf-8

class Solution:
        def findMissing(self, input, N):
                can = 0
                for i in range(1, N):
                        can ^= i
                for x in input:
                        can ^= x
                return can

if __name__=='__main__':
        input = [0,2,3]
        N = 4
        s = Solution()
        print s.findMissing(input, N)
