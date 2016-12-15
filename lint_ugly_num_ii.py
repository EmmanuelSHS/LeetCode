#!/usr/bin/env python
# coding=utf-8

class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        # ugly number generates from 3 sublist
        q = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        
        while len(q) < n:
            m2 = q[i2] * 2
            m3 = q[i3] * 3
            m5 = q[i5] * 5
            
            m = min(m2, m3, m5)
            # allow duplicates to go & append only once
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            q.append(m)
            
        print q
        return q[-1]
            

if __name__ == '__main__':
    s = Solution()
    print s.nthUglyNumber(10)
