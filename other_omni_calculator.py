#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        values = []
        ops = []
        i = 0
        while i < n:
            curr = s[i]
            if curr == ' ':
                continue

            if curr.isdigit():
                curr = int(curr)
                while i + 1 < n and s[i + 1].isdigit():
                    curr = curr * 10 + int(s[i + 1])
                    i += 1
                values.append(curr)
            elif curr == '(':
                ops.append(curr)
            elif curr == ')':
                while ops and ops[-1] != '(':
                    values.append(self.apply(ops.pop(), values.pop(), values.pop()))
                ops.pop()
            elif curr in '+-*/':
                while ops and self.hasPrecedence(curr, ops[-1]):
                    values.append(self.apply(ops.pop(), values.pop(), values.pop()))
                ops.append(curr)
            i += 1

        while ops:
            values.append(self.apply(ops.pop(), values.pop(), values.pop()))

        return values.pop()

    def hasPrecedence(self, op1, op2):
        if op2 in '()':
            return False
        if op1 in '*/' and op2 in '+-':
            return False
        else:
            return True

    def apply(self, op, b, a):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            if b == 0:
                return -1
            isNeg = a * b < 0
            return abs(a) / abs(b) if not isNeg else -1 * (abs(a) / abs(b))
        return 0


if __name__ == '__main__':
    s = Solution()
    tasks=['3+2/5','(1+2*3)/(6-4)']
    for x in tasks:
        print s.calculate(x)
