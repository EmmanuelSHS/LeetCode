#!/usr/bin/env python
# coding=utf-8

class Color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def getR(self):
        return self.r

    def getG(self):
        return self.g

    def getB(self):
        return self.b


class MixtureChecker(object):
    maxvalue = 255
    minvalue = 0

    def isMixable(self, colors, target):
        """
        : colors: list[Color]
        : target: Color with RGB given
        : return: bool, able to reach or not
        """
        return self.mix(colors, target, 0, None, None, None)

    def mix(self, colors, target, idx, currR, currB, currG):
        flag = self.checkEqual(target, currR, currB, currG)

        if flag == True:
            return True

        if not flag and idx < len(colors):
            currcolor = colors[idx]
            nextR = currR + currcolor.getR() if currR else currcolor.getR()
            nextG = currG + currcolor.getG() if currG else currcolor.getG()
            nextB = currB + currcolor.getB() if currB else currcolor.getB()

            addedflag = self.mix(colors, target, idx + 1, nextR, nextB, nextG)
            if addedflag:
                return True
            noaddflag = self.mix(colors, target, idx + 1, currR, currB, currG)
            if noaddflag:
                return True
        return False


    def checkEqual(self, target, currR, currB, currG):
        if not currR or not currB or not currG:
            return False

        if currR > self.maxvalue:
            currR = self.maxvalue
        if currB > self.maxvalue:
            currB = self.maxvalue
        if currG > self.maxvalue:
            currG = self.maxvalue

        return target.getR() == currR and target.getB() == currB and target.getG() == currG
        

if __name__ == '__main__':
    color1 = Color(10, 20, 30)
    color2 = Color(100, 200, 255)
    color3 = Color(0, 100, 100)
    colors = [color1, color2, color3]
    
    targets = [Color(10, 120, 130), Color(0, 0, 0), Color(255,255, 255), Color(100, 255, 255), Color(110, 220, 30), Color(110, 255, 255)]

    checker = MixtureChecker()
    for target in targets:
        print checker.isMixable(colors, target)


