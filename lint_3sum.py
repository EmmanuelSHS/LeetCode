#!/usr/bin/env python
# coding=utf-8

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        res = []
        numbers.sort()
        for i in range(len(numbers) - 1):
            target = - numbers[i]
            p1 = i + 1
            p2 = len(numbers) - 1
            
            while True:
                if p1 == p2:
                    break
                if numbers[p1] + numbers[p2] > target:
                    p2 -= 1
                elif numbers[p1] + numbers[p2] < target:
                    p1 += 1
                else:
                    goal = [-target, numbers[p1], numbers[p2]]
                    if goal not in res:
                        res.append( goal )
                    p1 += 1
        return res