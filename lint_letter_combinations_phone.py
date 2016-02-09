#!/usr/bin/env python
# coding=utf-8

class Solution:
    # @param {string} digits A digital string
    # @return {string[]} all posible letter combinations
    def letterCombinations(self, digits):
        # Write your code here
        if not digits:
            return []
        dic = {"0":" ", "1":" ", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz" }
        res = []
        tmp = ""
        self.allComb(digits, dic, res, tmp, 0)
        return res
        
    def allComb(self, digits, dic, res, tmp, cdp):
        if cdp == len(digits):
            res.append(tmp)
            return 
        
        for i in range(len(dic[digits[cdp]])):
            tmp += dic[digits[cdp]][i]
            self.allComb(digits, dic, res, tmp, cdp + 1)
            tmp = tmp[:cdp]