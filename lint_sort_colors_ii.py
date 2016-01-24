#!/usr/bin/env python
# coding=utf-8

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        now_max = k
        now_min = 1
        
        sorted = 0
        
        # you have to get global & local pointers separated
        # use while better than for in dynamic updating p2
        p1 = 0
        p2 = len(colors) - 1
        while (sorted < k):
            i = p1
            while (i <= p2):
                print p1, p2
                print colors
                if colors[i] == now_max:
                    colors[i], colors[p2] = colors[p2], colors[i]
                    p2 -= 1
                elif colors[i] == now_min:
                    colors[i], colors[p1] = colors[p1], colors[i]
                    p1 += 1
                    i += 1
                else:
                    i += 1
            now_max -= 1
            now_min += 1
            sorted += 2

if __name__ == '__main__':
    array = [3,2,3,3,4,3,3,2,4,4,1,2,1,1,1,3,4,3,4,2]; k = 4
    s = Solution()
    s.sortColors2(array, k)
    print array
    
