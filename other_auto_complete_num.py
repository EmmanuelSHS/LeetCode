#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    end = '/'

    def __init__(self, dictionary):
        '''
        : dictionary: list[str]
        '''
        self.trie = {}
        for word in dictionary:
            self._add(word)

    def _add(self, word):
        d = self.trie
        for c in word:
            d = d.setdefault(c, {})

        d[self.end] = None

    def autoCompleteNum(self, s):
        '''
        :s: str
        :return: int, # auto complete
        '''
        count = 0
        d = self.trie
        for c in s:
            if c in d:
                d = d[c]
            else:
                return count

        # if reach here s in d
        count += self._getEndNum(d)

        return count

    def _getEndNum(self, d):
        count = 0
        
        #if not d:
        #    return count

        for k, v in d.items():
            if k == self.end:
                count += 1
            else:
                count += self._getEndNum(v) 

        return count


if __name__ == '__main__':
    tests = {
        # empty
        1: {'d': [], 'cases': ['']},
        # normal
        2: {'d': ['snapchat', 'snake', 'smoke', ''], 'cases': ['a', 's', 'sn', '']},
        # large
        3: {'d': [], 'cases': []}
    }

    for idx, v in tests.items():
        s = Solution(v['d'])
        for c in v['cases']:
            print idx, ':', s.autoCompleteNum(c)
