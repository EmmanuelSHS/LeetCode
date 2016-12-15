#!/usr/bin/env python
# coding=utf-8
import sys

class BinarySearch(object):
    def search(self, candidates, target):
        """
        : candidates: list[int] sorted, may have duplicates
        : target: int, target number to find in candidates
        : return: int of idx, -1 if not in candidates
        """
        start, end = 0, len(candidates) - 1

        while start <= end:
            mid = start + (end - start) / 2
            if candidates[mid] == target:
                end = mid
            elif candidates[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        if candidates[end] == target:
            return end
        else:
            return -1


if __name__ == '__main__':
    searcher = BinarySearch()
    #candidates = [0,1,2,3,3,4,5]
    candidates = [i for i in range(sys.maxint)]
    targets = [1, 3, 5, 6, sys.maxint - 1]

    for target in targets:
        print searcher.search(candidates, target)
