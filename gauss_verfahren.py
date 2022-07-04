import numpy as np;
import copy

class GaussJordanOperator:

    def __init__(self, matrix, vector) -> None:
        self.G = np.c_[matrix, vector]

    def findPivot(self, row):
        pivot = None
        index = 0
        while index < len(row):
            el = row[index]
            if el != 0:
                pivot = el
                break
            index += 1 
        return pivot, index

    def divideRowElementsByPivot(self, pivot, i):
        if pivot != 1:
            for j in range(len(self.G[i])):
                self.G[i][j] /= pivot

    def multiplyAndSubtract(self, pivot_i, i, generator):
        row = self.G[i]
        for j in generator:
            row2 = self.G[j]
            multiplier = row2[pivot_i]
            for ci in range(len(row)):
                self.G[j][ci] = self.G[j][ci] - self.G[i][ci]*multiplier

    def applyTolerance(self, i, tol):
        for j in range(len(self.G[i])):
            if np.abs(self.G[i][j]) <= tol:
                self.G[i][j] = 0.0

    def partialPivotization(self, i):
        biggestRow = i
        for row in range(i+1,self.G.shape[0]):
            for col in range(self.G.shape[1] - 1):
                if np.abs(self.G[row][col]) > np.abs(self.G[biggestRow][col]):
                    biggestRow = row
        
        tmp = copy.deepcopy(self.G[i])
        for col in range(self.G.shape[1]):
            self.G[i][col] = self.G[biggestRow][col]
            self.G[biggestRow][col] = tmp[col]

    def run(self, mode="gauss", tol=-1):
        # mode gauss/jordan
        generator = range(len(self.G))

        if mode == "gauss":
            print("")
            print("Normal Gauss")
        else:
            print("")
            print("Gauss-Jordan")


        if tol < 0:
            tol = np.max(self.G.shape)*np.linalg.norm(self.G,ord=np.inf)*np.finfo(np.float64).eps

        if mode == "jordan":
            generator = reversed(range(1, len(self.G)))


        for i in generator:
            row = self.G[i]

            self.applyTolerance(i, tol)

            if mode == "gauss":
                self.partialPivotization(i)

            pivot, pivot_i = self.findPivot(row)

            if pivot == None:
                print("No pivot found")
                continue

            if mode == "gauss":
                self.divideRowElementsByPivot(pivot, i)

            if mode == "gauss" and i != len(self.G) - 1:
                self.multiplyAndSubtract(pivot_i, i, range(i+1, len(self.G)))
            if mode == "jordan":
                self.multiplyAndSubtract(pivot_i, i, reversed(range(0, i)))


matrix = [
            [2,1,0,2], 
            [4,2,3,3], 
            [-2,-1,6,-4],
            [-8,-4,9,-11],
            [2,1,-3,3]
        ]
vector = [6,16,2,-12,2]


gaussOpr = GaussJordanOperator(matrix, vector)
print("Anfangsmatrix")
print(gaussOpr.G)

gaussOpr.run("gauss")
print(gaussOpr.G)

gaussOpr.run("jordan")
print(gaussOpr.G)

