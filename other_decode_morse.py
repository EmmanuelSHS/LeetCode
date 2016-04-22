#!/usr/bin/env python
# coding=utf-8

class Solution:
        def __init__(self):
                self.morseAlphabet ={
                        "A" : ".-",
                        "B" : "-...",
                        "C" : "-.-.",
                        "D" : "-..",
                        "E" : ".",
                        "F" : "..-.",
                        "G" : "--.",
                        "H" : "....",
                        "I" : "..",
                        "J" : ".---",
                        "K" : "-.-",
                        "L" : ".-..",
                        "M" : "--",
                        "N" : "-.",
                        "O" : "---",
                        "P" : ".--.",
                        "Q" : "--.-",
                        "R" : ".-.",
                        "S" : "...",
                        "T" : "-",
                        "U" : "..-",
                        "V" : "...-",
                        "W" : ".--",
                        "X" : "-..-",
                        "Y" : "-.--",
                        "Z" : "--..",
                        " " : "/"
                        
                }
                self.inverseMorse = dict( (v, k) for (k, v) in self.morseAlphabet.items() )
                self.count = 0

        def decode(self, s):
                res = []
                tmp = []
                n = len(s)
                if n == 0:
                        return res
                self.getAll(s, res,tmp, 0, n)
                return res

        def getAll(self, s, res, tmp, start, end):
                print '1'
                self.count += 1
                print self.count
                print '2'
                if start == end:
                        print 'end',tmp
                        res.append(tmp[:])
                        return
                print '3'
                for i in range(start+1, end+1):
                        print '4'
                        deco = self.inverseMorse.get(s[start:i], False)
                        if not deco:
                                continue
                        print '5'
                        print deco
                        tmp.append(deco[:])
                        print 'before',tmp
                        self.getAll(s, res, tmp, i, end)
                        print 'after',tmp
                        tmp.pop()

if __name__=='__main__':
        testCode="......-...-..---/-...-...-..-.--/.--..-.---"
        testCode = "....."
        s = Solution()
        print s.decode(testCode)




