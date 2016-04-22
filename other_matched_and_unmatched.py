#!/usr/bin/env python
# coding=utf-8


class Solution:

    def diffAndSimilar(self, s1, s2):
        if not s1 or not s2:
            return 0, 0
        dict = {}
        sc, dc = 0, 0

        for i in range(len(s1)):
            if s1[i] not in dict:
                dict[s1[i]] = [i]
            else:
                dict[s1[i]].append(i)

        for i in range(len(s2)):
            loc = dict.get(s2[i], None)
            if not loc:
                continue
            if i in loc:
                sc += 1
            elif i not in loc:
                dc += 1
        return "similar counts " + \
            str(sc) + " different counts " + str(dc) + "\n"

if __name__ == '__main__':
    s = Solution()
    s1 = 'aadc'
    s2 = 'aaad'
    print s.diffAndSimilar(s1, s2)
