#!/usr/bin/env python
# coding=utf-8

class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    Make advantage of %'s property, (a * b) % p = (a % p) * (b % p) % p
    """
    def fastPower(self, a, b, n):
        # write your code here
        if a == 1:
            return 1 % b
        if n == 1:
            return a % b
        if n == 0:
            return 1 % b
        
        mod = self.fastPower(a, b, n/2)
        res = (mod % b)
        res *= res
        if n%2 == 1:
            res *= a % b
        return res % b
