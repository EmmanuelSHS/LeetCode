#!/usr/bin/env python
# coding=utf-8

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        # write your code here
        visited = [ [False for x in board[0]] for y in board ]
        nx = len(board)
        ny = len(board[0][:])
        for i in range(nx):
            for j in range(ny):
                if (self.trackWord(board, visited, word, 0, i, j)): 
                    return True
        return False
        
    def trackWord(self, board, visited, word, cwp, i, j):
        if cwp == len(word):
            return True
        
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1: 
            return False
        if visited[i][j] or board[i][j] != word[cwp]:
            return False
        
        visited[i][j] = True
        if self.trackWord(board, visited, word, cwp + 1, i - 1, j): 
            return True
        if self.trackWord(board, visited, word, cwp + 1, i + 1, j): 
            return True
        if self.trackWord(board, visited, word, cwp + 1, i, j - 1): 
            return True
        if self.trackWord(board, visited, word, cwp + 1, i, j + 1): 
            return True
        visited[i][j] = False
        return False