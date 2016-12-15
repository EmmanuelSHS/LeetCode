#!/usr/bin/env python
# coding=utf-8

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class LowestCommonAncester(object):
    def findAncester(self, root):
        """
        : root: TreeNode, root node of the tree
        : candidates: set(TreeNode)
        : return: the label of lca
        """
        # validity check
        if root == None:
            return None

        return self.traverse(root, 0)[0]

    def traverse(self, root, depth):
        if not root:
            return None, None

        if not root.left and not root.right:
            return root.val, depth

        leftancester, ldepth = self.traverse(root.left, depth + 1)
        rightancester, rdepth = self.traverse(root.right, depth + 1)

        if not leftancester and rightancester:
            return rightancester, rdepth
        if not rightancester and leftancester:
            return leftancester, ldepth
        if leftancester and rightancester:
            if ldepth == rdepth:
                return root.val, ldepth
            if ldepth > rdepth:
                return leftancester, ldepth
            if rdepth < rdepth:
                return rightancester, rdepth



if __name__ == '__main__':
    # construct tree
    # test case 1: imbalanced tree
    tn1 = TreeNode(1)
    tn2 = TreeNode(2)
    tn3 = TreeNode(3)
    tn4 = TreeNode(4)
    tn5 = TreeNode(5)
    tn6 = TreeNode(6)

    #tn1.left = tn2
    #tn1.right = tn3
    #tn2.left = tn4
    #tn4.left = tn5
    #tn4.right = tn6

    # test case 2: balanced
    tn1.left = tn2
    tn1.right = tn3
    tn2.left = tn4
    tn2.right = tn5
    tn3.left = tn6


    # test case 3: only one

    ancesterChecker = LowestCommonAncester()

    print ancesterChecker.findAncester(tn1)
