#!/usr/bin/env python
# coding=utf-8

class Solution:	
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        # write your code here
        num = sorted([str(x) for x in num], cmp = self.compare)
        res = ''.join(num).lstrip('0')
        return res or '0'
        
    def compare(self, a, b):
        # is only because default sorted is in ascending order
        if a + b > b + a:
            return -1
        else: return 1
        
if __name__ == '__main__':
    s = Solution()
    input = [1, 20, 23, 4, 8]
    print s.largestNumber(input)
