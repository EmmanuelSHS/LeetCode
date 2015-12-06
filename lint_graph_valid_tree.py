#!/usr/bin/env python
# coding=utf-8

'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
'''

from Queue import LifoQueue

class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        if edges  == [] and n == 1:
            return True
        elif edges == []:
            return False

        visited = [-1 for i in range(0, n)]
        father = [-1 for i in range(0, n)]
        adjl = {i: [] for i in range(0, n)}
        q = LifoQueue()
        for edge in edges:
            i = max(edge)
            j = min(edge)
            adjl[i].append(j)
            adjl[j].append(i)
        
        q.put(0)
        visited[0] == 0
        count = 0
        while count < n:
            while q.empty() == False:
                u = q.get()
                #print u
                for i in adjl[u]:
                    if visited[i] == 1 and father[u] != i:
                        return False
                    if visited[i] == -1:
                        visited[i] = 0
                        father[i] = u
                        q.put(i)
                visited[u] = 1
                count += 1
            try:
                next = visited.index(-1)
                print next
            except:
                return True
            visited[next] = 0
            q.put(next)
        return True

s = Solution()
# True instance
print s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
# False instance
print s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
# Robust check
print s.validTree(10, [[0,1],[5,6],[6,7],[9,0],[3,7],[4,8],[1,8],[5,2],[5,3]])
