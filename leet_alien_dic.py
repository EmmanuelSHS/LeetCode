#!/usr/bin/env python
# coding=utf-8

# not considering edge cases
class Solution:
        def alienOrder(self, list):
                post = {}
                visited = {}
                # init
                for word in list:
                        for c in word:
                                visited[c] = False
                # get all posterior
                for i in range(1, len(list)):
                        prev = list[i - 1]
                        curr = list[i]
                        l1 = len(prev)
                        l2 = len(curr)
                        j = 0
                        while j < min(l1, l2):
                                if prev[j] != curr[j]:
                                        if prev[j] not in post:
                                                post[ prev[j] ] = [ curr[j] ]
                                        else:
                                                post[ prev[j] ].append(curr[j])
                                j += 1
                # get topo order
                res = self.getOrder("", post, visited)
                return res

        def getOrder(self, res, post, visited)
                for start in post:
                        if not visited[start]:
                                for p in post[start]:
                                        # cycle
                                        if visited[p]:
                                                return ""
                                        self.getOrder()

if __name__=='__main__':
        can = [
                  "wrt",
                  "wrf",
                  "er",
                  "ett",
                  "rftt"

        ]
        s = Solution()
        print s.alienOrder(can)
