#!/usr/bin/env python
# coding=utf-8

class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    def updateBits(self, n, m, i, j):
        # write your code here
        
        # if j - i + 1 < len( (M)2 )
        
        # else
        ones = ~0
        mask = 0
        
        if (j < 31):
            left = ones << (j + 1)
            right = ((1 << i) - 1)
            mask = left | right
        else:
            mask = ((1 << i) - 1)
        print "{0:b}".format(mask)
            
        return (n & mask) | (m << i)

if __name__ == '__main__':
    s = Solution()
    print s.updateBits(456,31,27,31)
