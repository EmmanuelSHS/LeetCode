#!/usr/bin/env python
# coding=utf-8

'''
small range k, integer assumption
'''
def coutingsort(A, B, k):
    C = [0 for i in range(k + 1)]
    for i in A:
        C[i] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    for i in A:
        B[C[i]] = i
        C[i] -= 1

if __name__ == '__main__':
    a = [1,2, 4, 3, 1 ,1, 0, 9, 8]
    b = [0 for i in range(len(a) + 1)]
    # notice the referencing
    coutingsort(a, b, max(a))
    print b
