#!/usr/bin/env python
# coding=utf-8
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
class Solution:
    # @param {int} n n pairs
    # @return {string[]} All combinations of well-performed parentheses
    def get(self, res, paren, left, right):
        if (left == 0 and right == 0):
            res.append(paren)
        if (left > 0):
            self.get(res, paren + '(', left - 1, right)
            """
            not a if-else relation:
                if-else indicates tht left should be 0 before new right could be added.
            """
        # & is binary operator in python
        if (right > 0 and left < right):
            self.get(res, paren + ')', left, right - 1)

    def generateParenthesis(self, n):
        # init: leftmost & rightmost should always be ()
        res = []
         
        if (n <= 0):
            return res

        self.get(res, "", n, n)
        return res


s = Solution()
print s.generateParenthesis(3)
