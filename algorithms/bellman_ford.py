#!/usr/bin/env python
# coding=utf-8
import sys

class BellmanFord:
    MAX = 10000
    graph = {}
    dist = dict()
    prev = dict()

    def update(self,i, j):
        d = self.dist[i] + self.graph[i][j]
        if self.dist[j] > d:
            self.dist[j] = d
            self.prev[j] = i

    def run(self, graph, source, step):
        self.graph = graph
        n = len(self.graph)
        for i in self.graph.keys():
            self.dist.setdefault(i, self.MAX)
            self.prev.setdefault(i, self.MAX)
        self.dist[source] = 0

        for i in range(1, step):
            for i in self.graph.keys():
                try:
                    for j in self.graph[i].keys():
                        self.update(i, j)
                except Exception, e:
                    print e
                    print "has no edge ", i
                    continue

        print self.dist

if __name__ == '__main__':
    source = sys.argv[1]
    step = int(sys.argv[2])
    b = BellmanFord()
    G = {'s':{'a':4, 'b':5},
         'a':{'b':-1, 'c':1},
         'c':{},
         'b':{'a':2, 'c':-1}}
    b.run(G, source, step)
