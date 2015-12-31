#!/usr/bin/env python
# coding=utf-8

from max_heap import max_heap

class max_priority_queue(max_heap):

    NINF = -10000000

    def __init__(self, list, heap_size):
        max_heap.__init__(self, list, heap_size)
        self.build_max_heap()

    '''
    insert and maintain max heap properties
    '''
    def insert(self, key):
        self.heap_size += 1
        # TODO: if heap_size != length, have to move all non-heaps to their rights
        self.list[self.heap_size] = self.NINF
        self.increase_key(self.heap_size, key)

    def extract_max(self):
        if self.heap_size < 1:
            raise "Heap Underflow"
        max = self.list[1]
        self.list[1] = self.list[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(1)
        return max

    '''
    increase a key, then maintain max heap properties by up-comparision
    '''
    def increase_key(self, i, key):
        if key < self.list[i]:
            raise "new key is smaller than current key"
        self.list[i] = key
        while i > 1 and self.list[self.parent(i)] < self.list[i]:
            self.list[i] ^= self.list[self.parent(i)]
            self.list[self.parent(i)] ^= self.list[i]
            self.list[i] ^= self.list[self.parent(i)]
            i = self.parent(i)

    def maximum(self):
        self.list[1]

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    mpq = max_priority_queue(a, 4)
    print mpq.get_heap()
    mpq.insert(50)
    print mpq.get_heap()
