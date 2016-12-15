#!/usr/bin/env python
# coding=utf-8

"""
a set of solver for matrix multiplication

Base Hypothesis: n * m and all based on 2
    Suppose square matrix
"""

class Multiplier:
    """
    implementation should care greatly about how to add matrix on top of list
    how to slice list to desired matrix
    and how to merge result slices to complete matrix

    another way, make matrix a class, encapuslate operators in to class
    """
    def sliceMatrix(self, M, rs, cs):
        n = len(M)
        res = [ [0 for _ in range(n/2)] for _ in range(n/2) ]
        
        r, c = rs, cs
        for i in range(n / 2):
            for j in range(n / 2):
                res[i][j] = M[r][c]
                c += 1
            r += 1

        return res

    def addMatrix(self, M1, M2):
        n, m = len(M1), len(M1[0])
        return [[M1[i][j] + M2[i][j] for j in range(m)] for i in range(n)]

    def mergeMatrix(self, c11, c12, c21, c22, n):
        C = [ [0 for _ in range(n)] for _ in range(n)]

        for i in range(n / 2):
            for j in range(n / 2):
                C[i][j] = c11[i][j]
                C[i + n/2][j] = c12[i][j]
                C[i][j + n/2] = c21[i][j]
                C[i + n/2][j + n/2] = c22[i][j]
        return C

    def simple(self, A, B):
        # square matrix
        n = len(A)
        if n == 1:
            return [[ A[0][0] * B[0][0] ]]

        a11 = self.sliceMatrix(A, 0, 0) 
        a12 = self.sliceMatrix(A, 0, n/2) 
        a21 = self.sliceMatrix(A, n/2, 0) 
        a22 = self.sliceMatrix(A, n/2, n/2) 

        b11 = self.sliceMatrix(B, 0, 0) 
        b12 = self.sliceMatrix(B, 0, n/2) 
        b21 = self.sliceMatrix(B, n/2, 0) 
        b22 = self.sliceMatrix(B, n/2, n/2) 

        c11 = self.addMatrix(self.simple(a11, b11), self.simple(a12, b21))
        c12 = self.addMatrix(self.simple(a11, b12), self.simple(a12, b22))
        c21 = self.addMatrix(self.simple(a21, b11), self.simple(a22, b21))
        c22 = self.addMatrix(self.simple(a21, b12), self.simple(a22, b22))

        return self.mergeMatrix(c11, c12, c21, c22, n)
        
    def strassen(self):
        pass


if __name__ == '__main__':
    A = [[1, 2], [3, 4]]
    B = [[1, 2], [3, 4]]
    solver = Multiplier()
    print solver.simple(A, B)
