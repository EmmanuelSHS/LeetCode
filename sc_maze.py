#!/usr/bin/env python
# coding=utf-8

import Queue


# 0 = walkable
# 5 = block
# 1 = beginning, always (0,0)
# 9 = destination

# return: "Bagel", "No dice"
# [0, 1]

class MazeSolver(object):
    walkable = 0
    block = 5
    destination = 9
    success = "Bagel"
    failure = "No dice"

    def hasPath(self, array):
        """
        : array: list[list[int]] valid maze
        : return: "Bagel" if find a path, "No dice" if not
        """
        # init
        n = len(array)
        m = len(array[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        traversed = [[False for i in range(m)] for j in range(n)]
        """
        paths:
            key: identifier for curr position
            value: set((x, y)) for prev position
        """
        paths = {}
        q = Queue.Queue()

        # add start pos
        q.put((0, 0))
        while q.qsize() != 0:
            x, y = q.get()
            # mark traversed
            traversed[x][y] = True
            # if reach the destination
            if array[x][y] == self.destination:
                path = self.reconstruct(paths, x, y)
                return self.success, path

            # possible next directions
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx and nx < n and 0 <= ny and ny < m and traversed[nx][ny] == False and array[nx][ny] != self.block:
                    # add to queue
                    q.put((nx, ny))
                    # add to path
                    idf = str((nx, ny))
                    paths[idf] = paths.get(idf, set()) | {(x, y)}

        return self.failure, []

    def reconstruct(self, paths, x, y):
        if x == 0 and y == 0:
            return [[0, 0]]

        idf = str((x, y))
        path = []
        for prevx, prevy in paths[idf]:
            path = self.reconstruct(paths, prevx, prevy)
            if path != []:
                path.append([x, y])
                break

        return path


if __name__ == '__main__':
    array1 = [[1, 5, 5, 5, 5],
             [0, 5, 0, 0, 0],
             [0, 5, 0, 5, 0],
             [0, 0, 0, 5, 0],
             [0, 5, 5, 5, 9]
            ]

    array2 = [[1, 5, 5, 5, 9],
             [0, 5, 0, 0, 0],
             [0, 5, 0, 5, 0],
             [0, 0, 0, 5, 0],
             [0, 5, 5, 5, 5]
            ]

    array2 = [[1, 5, 5, 5, 9],
             [0, 5, 0, 0, 0],
             [0, 5, 0, 5, 0],
             [0, 5, 0, 5, 0],
             [0, 5, 5, 5, 5]
            ]

    solver = MazeSolver()

    for maze in [array1, array2]:
        print solver.hasPath(maze)


