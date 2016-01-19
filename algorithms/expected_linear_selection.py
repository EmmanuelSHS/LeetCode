#!/usr/bin/env python
# coding=utf-8

import random

'''
why ## part could only return i-th smallest,
these two swap have so great differences

this changes not real value
def swap(x, y):
    tmp = x
    x = y
    y = tmp
'''
    
def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    
def rpartition(A, p, r):
    random.seed(1234)
    i = random.randrange(p, r)
    swap(A, i, r)

    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
        #if x < A[j]:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1

'''
randomized select, select i-th smallest, i from 1, 2 ...
'''
def rselect(A, p, r, i):
    if p == r:
        return A[p]
    q = rpartition(A, p, r)
    print q, A
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return rselect(A, p, q-1, i)
    else:
        return rselect(A, q+1, r, i-k)

if __name__ == '__main__':
    a = [0, 6, 2, 1, 4, 3]
    print rselect(a, 0, 5, 5)
    print rselect(a, 1, 5, 5)
