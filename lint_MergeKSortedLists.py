#!/usr/bin/env python
# coding=utf-8

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        n = len(lists)
        if not lists:
            return None
        return self.merge(lists, 0, n-1)
        
    def merge(self, lists, head, tail):
        if head == tail:
            return lists[head]
        mid = (head + tail) / 2
        leftList = self.merge(lists, head, mid)
        rightList = self.merge(lists, mid+1, tail)
        return self.mergeTwo(leftList, rightList)
        
    def mergeTwo(self, leftList, rightList):
        head = ListNode(0)
        tail = head
        
        while leftList and rightList:
            if leftList.val <= rightList.val:
                tail.next = leftList
                tail = leftList
                leftList = leftList.next
            else:
                tail.next = rightList
                tail = rightList
                rightList = rightList.next
        
        tail.next = rightList if not leftList else leftList
        
        return head.next
        
                
                
