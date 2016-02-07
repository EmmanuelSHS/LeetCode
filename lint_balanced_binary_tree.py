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
    @return: True if this Binary tree is Balanced, or false.
    key point is which stands for the depth of current node
    """
    def isBalanced(self, root):
        # write your code here
        
        flag, depth = self.IsBalanced(root, 0)
        return flag
        
    def IsBalanced(self, root, layer):
        if not root:
            return True, layer
            
        lflag, ldepth = self.IsBalanced(root.left, layer + 1)
        rflag, rdepth = self.IsBalanced(root.right, layer  + 1)
        delta = ldepth - rdepth
        
        return (lflag and rflag and delta < 2 and delta > -2), max(ldepth, rdepth)
