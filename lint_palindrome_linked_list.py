#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        # Write your code here
        if not head:
            return True

        p1 = p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
            
        prev, p3 = None, p1.next
        while p3:
            tmp = p3.next
            p3.next = prev
            prev = p3
            p3 = tmp
            
        p4 = head
        while prev:
            if p4.val != prev.val:
                return False
            prev = prev.next
            p4 = p4.next
            print prev.val, p4.val
        return True

if __name__ == '__main__':
        head = ListNode(1);
        l1 = ListNode(0); head.next  = l1
        l2 = ListNode(3); l1.next = l2
        l3 = ListNode(4); l2.next = l3
        l4 = ListNode(0); l3.next = l4
        tail = ListNode(1); l4.next = tail
        s = Solution()
        print s.isPalindrome(head)
