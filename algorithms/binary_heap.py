#!/usr/bin/env python
# coding=utf-8

from copy import deepcopy

class binary_heap:
    def __init__(self, list, heap_size):
        # self.list = list.insert() get the return of insert function, not list
        # dont use pointer/shallow copy/referencing
        self.list = deepcopy(list); self.list.insert(0, ' ')
        self.heap_size = heap_size
        self.length = len(list)

    '''
    figure out diff of update and insert
    def insert(self, x):
        self.list.append(x)
        # TODO: if i insert sth new into heap end while this end is not array end
        self.heap_size += 1
        if self.heap_size == self.length:
            self.length += 1
    '''

    '''
    for those s.t. start with i = 0, left & right won't work pretty well as sudocode in textbook suggest
    '''
    def parent(self, i):
        return i / 2

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def get_heap(self):
        return self.list[1:]

    def get_size(self):
        return self.heap_size

    def get_len(self):
        return self.length

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    bh = binary_heap(a, 5)
    print bh.get_heap()
    print bh.get_size()
    print bh.get_len()
