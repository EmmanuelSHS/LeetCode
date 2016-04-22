#!/usr/bin/env python
# coding=utf-8

class Solution:
    # @param {string[]} tokens The Reverse Polish Notation
    # @return {int} the value
    def evalRPN(self, tokens):
        # Write your code here
        n = len(tokens)
        if n == 1:
            return int(tokens[0])
        stack = []
        cal = ['+', '-', '*', '/']
        for x in tokens:
            if x not in cal:
                stack.append(int(x))
            else:
                print stack
                n1 = stack.pop()
                n2 = stack.pop()
                if x == '+':
                    stack.append(n2 + n1)
                elif x == '-':
                    stack.append(n2 - n1)
                elif x == '*':
                    stack.append(n2 * n1)
                elif x == '/':
                    stack.append(int( float(n2) / n1 ) )
        return stack.pop()

if __name__ == '__main__':
        t = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        s = Solution()
        print s.evalRPN(t)
            
