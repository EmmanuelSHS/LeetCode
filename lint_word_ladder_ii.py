#!/usr/bin/env python
# coding=utf-8

from collections import deque
from input_word_ladder_ii import START, END, DICT
import time

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    
    def findLaddersI(self, start, end, dict):
        # write your code here
        res = []
        n = len(start)
        
        prevD = -1
        maxD = -1
        prevWords, currWords = [], set([start])
        
        dict.add(end)
        q = deque()
        q.append([start, [start], 0])
        
        # 
        while q:
            currPair = q.popleft()
            currW = currPair[0]
            currP = currPair[1]
            currD = currPair[2]
                        
            if currD >= maxD + 1 and maxD != -1:
                break
            
            if prevD != currD:
                prevD = currD
                if not currWords:
                    return res
                for w in currWords:
                    dict.remove(w)
                #prevWords = currWords
                currWords = set()
                    
            if currW == end:
                if maxD == -1:
                    maxD = currD
                if currD <= maxD:
                    res.append(currP)
            else:
                if currD >= maxD and maxD != -1:
                    continue
                for i in range(n):
                    p1 = currW[:i]
                    p2 = currW[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newW = p1 + c + p2
                        if c != currW[i]:
                            if newW in dict:
                                currWords.add(newW)
                                q.append([newW, currP + [newW], currD + 1])
                            
        return res

    def findLaddersII(self, start, end, dict):
        def buildpath(path, word):
            if len(prevMap[word])==0:
                path.append(word); currPath=path[:]
                currPath.reverse(); result.append(currPath)
                path.pop();
                return
            path.append(word)
            for iter in prevMap[word]:
                buildpath(path, iter)
            path.pop()
        
        result=[]
        prevMap={}
        length=len(start)
        for i in dict:
            prevMap[i]=[]
        candidates=[set(),set()]; current=0; previous=1
        candidates[current].add(start)
        while True:
            current, previous=previous, current
            for i in candidates[previous]: 
                if i in dict:
                    dict.remove(i)
            candidates[current].clear()
            for word in candidates[previous]:
                for i in range(length):
                    part1=word[:i]; part2=word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i]!=j:
                            nextword=part1+j+part2
                            if nextword in dict:
                                prevMap[nextword].append(word)
                                candidates[current].add(nextword)
            if len(candidates[current])==0: return result
            if end in candidates[current]: break
        buildpath([], end)
        return result


if __name__ == '__main__':
    s = Solution()
    t1 = time.time()
    s.findLaddersI(START, END, DICT)
    t2 = time.time()
    print t2 - t1
    s.findLaddersII(START, END, DICT)
    t3 = time.time()
    print t3 - t2

