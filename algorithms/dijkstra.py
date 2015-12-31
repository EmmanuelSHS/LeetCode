#!/usr/bin/env python
# coding=utf-8


class Dijkstra:
    def distmin(self, dist, Q):
        mindex = ''
        dmin = 10000
        for x in Q:
            if dist[x] < dmin:
                mindex = x
                dmin = dist[x]
        return mindex

    def run(self, graph, source):
        n = len(graph)
        dist = [1000 for i in range(0, n)]
        prev = [-1 for i in range(0, n)] 
        Q = [i for i in range(0, n)]

        dist[source] = 0

        u = source
        while len(Q) != 0:
            u = self.distmin(dist, Q)
            # all the pop happens here
            # otherwise this u is not source in the beginning
            Q.pop(Q.index(u))

            for j in range(0, n):
                if graph[u][j] != 0 and j in Q:
                    d = dist[u] + graph[u][j]
                    if d < dist[j]:
                        dist[j] = d
                        prev[j] = u

        return dist, prev

dj = Dijkstra()
G = [[0, 7, 9, 0, 0, 14],
     [7, 0, 10, 15, 0, 0],
     [9, 10, 0, 11, 0, 2],
     [0, 15, 11, 0, 6, 0],
     [0, 0, 0, 6, 0, 9],
     [14, 0, 2, 0, 9, 0]]
print dj.run(G, 0)
