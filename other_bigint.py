#!/usr/bin/env python
# coding=utf-8

class BigInt:

    def add(self, x, y):
        """
        : x, str input as int
        : y, str input as int
        : ret: str of x + y
        """
        ix = len(x) - 1
        iy = len(y) - 1
        carry = 0
        base = 10
        res = ''

        while ix >= 0 or iy >= 0 or carry != 0:
            curr = carry
            curr = curr + int(x[ix]) if ix >= 0 else curr
            curr = curr + int(y[iy]) if iy >= 0 else curr
            carry = curr / base
            res += str(curr % base)

            ix -= 1
            iy -= 1

        return res[::-1]

if __name__ == '__main__':
    xs = ['', '0', '12345']
    ys = ['1', '2', '12345']
    bi = BigInt()

    for x, y in zip(xs, ys):
        print bi.add(x, y)

