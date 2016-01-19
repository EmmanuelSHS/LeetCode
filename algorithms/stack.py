#!/usr/bin/env python
# coding=utf-8

import copy

class stack:
    
    def __init__(self, list, maxlen):
        self.top = len(list) - 1
        self.maxlen = maxlen
        self.list = copy.deepcopy(list)

    def empty(self):
        return True if self.top == -1 else False

    def push(self, x):
        if isinstance(x, int):
            if self.top + 2 <= self.maxlen:
                self.list.append(x)
                self.top += 1
            else:
                raise "Error: Stack Overflow!"
        else:
            raise "Error: Only int number is acceptable!"

    def pop(self):
        if self.top == -1:
            raise "Error: Stack Underflow!"
        else:
            self.top -= 1
            return self.list.pop()

    def getstack(self):
        return self.list

    def gettop(self):
        return self.top

if __name__ == '__main__':
    s = stack([], 10)
    print s.getstack()
    print s.gettop()
    s.push(1); print s.getstack()
    print s.pop()
