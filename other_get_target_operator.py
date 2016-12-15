#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def isPossibleTarget(self, nums, target):
        '''
        : nums: list[int] candidate numbers for + - *
        : target: int target number to be reached
        : return: bool whether can reach target
        '''
        n = len(nums)
        if n == 0 or n == 1 and nums[0] != target:
            return False

        '''
        currtarget = set()
        currtarget.add((nums[0], None))
        # O(3^n)
        for i in range(1, n):
            x = nums[i]
            tmptarget = set()
            for val, prev in currtarget:
                tmptarget.add((val + x, x))
                tmptarget.add((val - x, -x))
                if prev == None:
                    tmptarget.add((val * x, None))
                else:
                    tmptarget.add((val - prev + prev * x, None))
            currtarget = tmptarget

        return target in [val for val, _ in currtarget]
        '''
        nops = 3
        sums = [set() for _ in range(nops)]
        ad, mn, ts = [i for i in range(nops)]

        for i in range(n):
            if i == 0:
                for i in range(nops):
                    sums[i].add(nums[i])
            else:
                tmpsums = [set() for _ in range(nops)]
                for i in range(nops):
                    for j in range(nops):
                        pass


if __name__ == '__main__':
    s = Solution()
    tests = {
        1: {'nums': [1, 2, 4], 'targets': [-1, -7, 6, 1000]},
        2: {'nums': [i for i in range(1000)], 'targets': [i for i in range(0, 1000, 100)]}
    }

    for i, test in tests.items():
        print i 
        for target in test['targets']:
            print s.isPossibleTarget(test['nums'], target)

