#!/usr/bin/env python
# coding=utf-8

def insert_sort(A):
    for i in range(1, len(A)):
        for j in range(i):
            if A[j] > A[i]:
                tmp = A[i]
                A[i] = A[j]
                A[j] = tmp

if __name__ == '__main__':
    a = [0, 3, 4, 2, 1, 7, 8, 5]
    insert_sort(a)
    print a
