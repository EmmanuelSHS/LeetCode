#!/usr/bin/env python
# coding=utf-8

import sys

"""
The key point is that adjacent makes cross max possible, makes d-c possible
"""
class Solution:
    """
    two solutions:
        O(nlogn) ordinary divide-and-conquer
        O(n) only return maxsum, could extend to know l, r pos; use local-
            global sum relationship; also possible for all neg, since set 0 
            is in the very beg;
    """
    def maxSubarrayN(self, A):
        if not A:
            return 0
        
        thissum = 0
        gsum = -sys.maxint
        
        l, r = 0, 0
        for i, x in enumerate(A):
            # drop thissum < 0 since neg sum is due to be abandoned
            if thissum < 0:
                thissum = 0
                l = i
            thissum += x
            if gsum < thissum:
                gsum = thissum
                r = i
            #gsum = max(gsum, thissum)

        return l, r, gsum


    def maxSubarrayNS(self, A):
        if not A:
            return 0

        return self.findMaxSubarray(A, 0, len(A) - 1)

    def findMaxSubarray(self, A, start, end):
        if start == end:
            return start, end, A[start]

        mid = (start + end) / 2 # right from mid + 1 to end
        ll, lh, ls = self.findMaxSubarray(A, start, mid)
        rl, rh, rs = self.findMaxSubarray(A, mid + 1, end)
        ml, mh, ms = self.findCrossMax(A, start, mid, end)

        if ls >= rs and ls >= ms:
            return ll, lh, ls
        elif rs >= ls and rs >= ms:
            return rl, rh, rs
        else:
            return ml, mh, ms

    def findCrossMax(self, A, start, mid, end):
        lsum = -sys.maxint
        rsum = -sys.maxint

        l = mid
        r = mid

        # left bound
        sum = 0
        for i in range(mid, start - 1, -1):
            sum += A[i]
            # no need to break here
            if sum > lsum:
                lsum = sum
                l = i

        # right bound
        sum = 0
        for i in range(mid + 1, end + 1):
            sum += A[i]
            # no need to break here
            if sum > rsum:
                rsum = sum
                r = i

        return l, r, lsum + rsum


if __name__ == '__main__':
    s = Solution()
    input = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print s.maxSubarrayNS(input)
    print s.maxSubarrayN(input)
            
    input = [1, 2, 3, 4, 5]
    print s.maxSubarrayNS(input)
    print s.maxSubarrayN(input)
