#!/usr/bin/env python
# coding=utf-8

from insert_sort import insert_sort

def bucketsort(A):
    res = []
    length = len(A)
    B = [[] for i in range(length)]
    for i in A:
        B[int(length * i)].append(i)
    for j in B:
        insert_sort(j)
        res.extend(j)
    return res

if __name__ == '__main__':
    A = [.55, .56, .43, .67, .78, .19, 0]
    print bucketsort(A)
