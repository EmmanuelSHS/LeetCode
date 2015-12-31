#!/usr/bin/env python
# coding=utf-8

from binary_heap import binary_heap

class max_heap(binary_heap):

    '''
    flow-down property, only works if list[i] is smaller than its children
    i.e. automatically stop after list[i] >= its children
    '''
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l <= self.heap_size and self.list[l] > self.list[i]:
            largest = l
        # compare both children
        if r <= self.heap_size and self.list[r] > self.list[largest]:
            largest = r
        if largest != i:
            self.list[i] ^= self.list[largest]
            self.list[largest] ^= self.list[i]
            self.list[i] ^= self.list[largest]
            self.max_heapify(largest)
   
    '''
    why i leave alone the other part?
    bottom to top, bottom successfully heapifies second last layer
    since start from 0, not heap_size/2 as sudo code suggest
    '''
    def build_max_heap(self):
        for i in range(self.heap_size/2, 0, -1):
            # print i
            self.max_heapify(i)

    '''
    let size = length for heap sort
    '''
    def heap_sort(self):
        self.size = self.length
        self.build_max_heap()
        for i in range(self.length, 1, -1):
            tmp = self.list[1]
            self.list[1] = self.list[i]
            self.list[i] = tmp
            self.heap_size -= 1
            self.max_heapify(1)

if __name__ == '__main__':
    a = [10, 20, 5, 6, 9, 111, 2, 3, 1, 6, 11]
    mh = max_heap(a, len(a))
    # mh.max_heapify(0)
    #mh.build_max_heap()
    #print mh.get_heap()
    #print mh.get_size()
    mh.heap_sort()
    print mh.get_heap()
