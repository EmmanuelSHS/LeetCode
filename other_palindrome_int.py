#!/usr/bin/env python
# coding=utf-8

class Solution:
        def isPalindrome(self, num):
                n = len(str(num))
                if n in [0, 1]:
                        return True
                p1, p2 = 0, n-1
                while p1 <= p2:
                        if str(num)[p1] != str(num)[p2]:
                                return False
                        p1 += 1
                        p2 -= 1
                return True

if __name__ == '__main__':
        s = Solution()
        print s.isPalindrome('')
        print s.isPalindrome(1)
        print s.isPalindrome(12)
        print s.isPalindrome(11)
        print s.isPalindrome(12321)
        print s.isPalindrome(1234)
