#!/usr/bin/env python
# coding=utf-8

class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        # write your code here
        p1 = 0
        p2 = len(chars) - 1
        
        while (p1 < p2):
            if chars[p1].isupper():
                chars[p1], chars[p2] = chars[p2], chars[p1]
                p2 -= 1
            else:
                p1 += 1
                
