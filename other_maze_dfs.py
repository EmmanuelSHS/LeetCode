#!/usr/bin/env python
# coding=utf-8

class InvalidMovement(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Invalid Movement Distance:", self.value


class Car(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPos(self):
        return self.x, self.y

    def move(self, dx, dy):
        if abs(dx) > 1 or abs(dy) > 1:
            raise InvalidMovement((dx, dy))
        self.x += dx
        self.y += dy


class Solution(object):
    path = 'p'
    wall = 'w'
    exit = 'e'
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def passMaze(self, maze, start):
        '''
        : maze: list[list[str]] path, wall, entrance, exit
        : start: tuple(int, int) start coordinates
        : return: bool = can / not
        '''
        x, y = start
        mycar = Car(x, y)
        self.traversed = set()
        if not maze:
            return False

        m = len(maze)
        n = len(maze[0])
        if 0 > x or x > m - 1 or 0 > y or y > n - 1 or maze[x][y] != self.path:
            return False

        return self._dfs(maze, mycar)

    def _dfs(self, maze, mycar):
        x, y = mycar.getPos()
        self.traversed.add((x, y))
        n, m = len(maze), len(maze[0])
        if maze[x][y] == self.exit:
            return True

        for dx, dy in self.dirs:
            mycar.move(dx, dy)
            nx, ny = mycar.getPos()
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in self.traversed and maze[nx][ny] != self.wall:
                flag = self._dfs(maze, mycar)
                if flag:
                    return flag
            mycar.move(-dx, -dy)

        return False


if __name__ == '__main__':
    s = Solution()
    tests = {
        1: {'maze':[['e', 'p', 'w', 'w', 'w', 'w'],
                    ['w', 'p', 'w', 'w', 'p', 'w'],
                    ['w', 'p', 'w', 'p', 'p', 'w'],
                    ['w', 'p', 'w', 'w', 'w', 'e'],
                    ['w', 'p', 'p', 'p', 'p', 'p'],
                    ['w', 'w', 'w', 'w', 'w', 'w'],
                   ], 
            'starts': [(0, 0), (-1, -1), (4, 4), (1, 1), (2, 1), (2, 3)]}
    }

    for idx, test in tests.items():
        for sid, start in enumerate(test['starts']):
            print idx, start, ':', s.passMaze(test['maze'], start)
