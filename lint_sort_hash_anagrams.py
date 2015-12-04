#!/usr/bin/env python
# coding=utf-8

class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        # dic is like a hashmap in python
        dic = {}
        res = []
        for i in strs:
            std = ''.join(sorted(i[:]))
            if (std in dic):
                dic[std].append(i)
            else:
                dic[std] = [i]

        for key in dic:
            if len(dic[key]) > 1:
                res.extend(dic[key])
        return res

strs = ['ab', 'ba', 'cd', 'dc', 'e']
s = Solution()
print s.anagrams(strs)
