#!/usr/bin/env python
# coding=utf-8

import sys


class MongeArray:

    minInMonge = []

    def findMinOneRow(self, candidate):
        p, m = 0, sys.maxint
        for i, x in enumerate(candidate):
            if x < m:
                m = x
                p = i
        
        return p, m

    def findMinEleMongeArray(candidate):
        n = len(candidate)
        if n == 1:
            return self,findMinOneRow(candidate)

        self.findMinEleMongeArray(candidate[::2])
