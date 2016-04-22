#!/usr/bin/env python
# coding=utf-8
import sys
class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    # key is consider init value
    def continuousSubarraySum(self, A):
        # Write your code here
        beg,end=0,0
        n=len(A)
        if n==0:
            return [beg,end]
        if n==1:
            return [beg,end]
        s, ts = -sys.maxint, 0
        for i in range(n):
            ts+=A[i]
            s=max(s,ts)
            if s==ts:
                end=i
            ts=max(0,ts)
            
        for i in range(end, -1, -1):
            s -= A[i]
            if s == 0:
                beg = i    
                break
        return [beg,end]

if __name__=='__main__':
        s = Solution()
        input = [-101,-33,-44,-55,-67,-78,-101,-33,-44,-55,-67,-78,-100,-200,-1000,-22,-100,-200,-1000,-22]
        print s.continuousSubarraySum(input)
