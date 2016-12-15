#!/usr/bin/env python
# coding=utf-8

import math

class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation(self, n):
        # write you code here
        # b may have less precision -> 6419 like
        (a, b) = n.split('.')
        a = '{:b}'.format(int(a))
        b = self.frac_to_binary(b)
        if b is None:
            return 'ERROR'
        elif b == '':
            return a
        else:
            return a + '.' + b
    
    def frac_to_binary(self, num):
        if int(num) == 0:
            return ''
        if int(num) % 10 != 5:
            return None
        
        res = ''
        num = float('0.' + str(num))
        while num:
            num *= 2
            if num >= 1:
                res += '1'
                num -= 1
            else:
                res += '0'
            if num and str(num)[-1] != '5':
                return None
                
        return res
        
if __name__ == '__main__':
    s = Solution()
    print s.binaryRepresentation("17817287.6418609619140625")
