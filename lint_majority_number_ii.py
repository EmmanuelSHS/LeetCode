#!/usr/bin/env python
# coding=utf-8

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    the greedy lies in the fact of 1/3, indicating a 3-a-group elimination
    """
    def majorityNumber(self, nums):
        # write your code here
        n1, n2 = None, None
        c1, c2 = 0, 0
        
        for x in nums:
            if x == n1:
                c1 += 1
            elif x == n2:
                c2 += 1
            elif c1 == 0:
                c1 = 1
                n1 = x
            elif c2 == 0:
                c2 = 1
                n2 = x
            else:
                c1 -= 1
                c2 -= 1
        
        c1, c2 = 0, 0       
        for x in nums:
            if x == n1:
                c1 += 1
            elif x == n2:
                c2 += 1
                
        return n1 if c1 > c2 else n2
                
            
