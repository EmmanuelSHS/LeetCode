#!/usr/bin/env python
# coding=utf-8

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    the key is that cross path sum couldn't be returned by allMax, need to store separately
    everytime return max from leaf till root
    """
    def maxPathSum(self, root):
        # write your code here
        res = [-1000]
        maxToRoot = self.allMax(root, res)
        return res[0]
    
    def allMax(self, root, res):
        if not root:
            return 0
        lmax = self.allMax(root.left, res) if root.left else 0
        pVal = root.val
        rmax = self.allMax(root.right, res) if root.right else 0
        maxToRoot = max(lmax + pVal, rmax + pVal, pVal)
        res[0] = max(res[0], maxToRoot, lmax + rmax + pVal)
        return maxToRoot