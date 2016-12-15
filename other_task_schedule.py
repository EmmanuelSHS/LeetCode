#!/usr/bin/env python
# coding=utf-8

import Queue


class MaxHeap(object):
    def __init__(self):
        self.q = Queue.PriorityQueue()
        
    def put(self, char, count):
        self.q.put((-count, char))
        
    def get(self):
        count, char = self.q.get()
        return char, -count
        
    def size(self):
        return self.q.qsize()


class Solution(object):
    def taskScheduler(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        d = {}
        for c in str:
            d[c] = d.get(c, 0) + 1
        
        h = MaxHeap()
        for key, val in d.items():
            h.put(key, val)
            
        q = Queue.Queue()
        res = ''
        i = 0
        while i < len(str):
            # in case no candidates
            if h.size() != 0:
                char, count = h.get()
                i += 1
            else:
                char, count = '_', 0
            res += char
            count -= 1
            
            q.put((char, count))
            if q.qsize() <= k:
                continue
            
            front, fcount = q.get()
            if fcount > 0:
                h.put(front, fcount)
                
        return res
        

if __name__ == '__main__':
    s = Solution()
    strs = ['aabbc', 'aaabc', 'aaadbbcc', 'AAABBB']
    ks = [3, 3, 2, 2]
    for str, k in zip(strs, ks):
        print str, k, '\n', s.taskScheduler(str, k), '\n'
