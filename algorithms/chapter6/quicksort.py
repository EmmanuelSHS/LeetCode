#!/usr/bin/env python
# coding=utf-8

from copy import deepcopy
import random

class quicksort():
    
    def __init__(self, list, rflag=False):
        self.list = deepcopy(list)
        self.rflag = rflag

    '''
    can rise bug if swap with oneself
    suitable for int
    '''
    def swap(self, i, j):
        if i != j:
            self.list[i] ^= self.list[j]
            self.list[j] ^= self.list[i]
            self.list[i] ^= self.list[j]

    '''
    ensure i + 1 is the middle number
    i add n times, equal to ##<than the end number
    each iter throw those #<than end to front
    inner order doesnt matter
    O(n)
    '''
    def partition(self, p, r):
        x = self.list[r]
        i = p - 1
        for j in range(p, r):
            #print x
            if self.list[j] <= x:
                i += 1
                #print i, j
                self.swap(i, j)
        #print 'i+1', i+1, 'r', r
        self.swap(i + 1, r)
        return i + 1

    def rpartition(self, p, r):
        random.seed(1234)
        i = random.randrange(p, r)
        self.swap(i, r)
        return self.partition(p, r)

    def sort(self, p, r):
        if p < r:
            q = self.rpartition(p, r) if self.rflag else self.partition(p, r)
            #print self.getsorted()
            self.sort(p, q-1)
            self.sort(q+1, r)

    def getsorted(self):
        return self.list

    def getflag(self):
        return self.rflag

if __name__ == '__main__':
    a = [6, 7, 1, 3, 4, 2222, 444433, 33333, 233, 0]
    qs = quicksort(a)
    qs.sort(0, len(a) - 1)
    print qs.getsorted()

    qs = quicksort(a, True)
    qs.sort(0, len(a) - 1)
    print qs.getsorted()
    print qs.getflag()


    qs = quicksort(a)
    print qs.getflag()
