#!/usr/bin/env python
# coding=utf-8

‘’’
If car starts at A and can not reach B. Any station between A and B can not reach B
‘’’
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        sdiff = 0
        start = 0
        ldiff = 0
        for i in range( len(gas) ):
            sdiff += gas[i] - cost[i]
            ldiff += gas[i] - cost[i]
            if ldiff < 0:
                start = i + 1
                ldiff = 0
                
        return start if sdiff >= 0 else -1