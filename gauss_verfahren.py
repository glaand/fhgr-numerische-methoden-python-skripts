import numpy as np;

A = np.array([[2.,1.,0.,2.],[4.,2.,3.,3.],[-2.,-1.,6.,-4.],[-8.,-4.,9.,-11.],[2.,1.,-3.,3.]])
b = np.array([6.,16.,2.,-12.,2.])
G = np.c_[A, b]
print("Startmatrix:")
print(G)
print("")
Glen = len(G)

def findPivot(row):
    print(f"Searching for pivot element in row: {row}")
    pivot = None
    index = 0
    while index < len(row):
        el = row[index]
        if el != 0:
            pivot = el
            break
        index += 1 
    return pivot, index

def divideRowElementsByPivot(pivot, i):
    row = G[i]
    print(f"Dividing elements of row by pivot({pivot}): {row}")
    if pivot != 1:
        for j in range(len(G[i])):
            G[i][j] /= pivot

def multiplyAndSubtract(pivot_i, i, generator):
    row = G[i]
    print(f"Multiply and subtract the pivot row: {row}")
    for j in generator:
        row2 = G[j]
        print(f"Target row: {row2}")
        multiplier = row2[pivot_i]
        print(f"Multiplier of row: {multiplier}")
        for ci in range(len(row)):
            G[j][ci] = G[j][ci] - G[i][ci]*multiplier

# Normal Gauss
for i in range(Glen):
    row = G[i]
    pivot, pivot_i = findPivot(row)

    if pivot == None:
        print("No pivot found")
        continue

    divideRowElementsByPivot(pivot, i)

    if i != Glen - 1:
        multiplyAndSubtract(pivot_i, i, range(i+1, len(G)))

# Gauss jordan
print("")
print("Gauss-Jordan")
for i in reversed(range(1, Glen)):
    row = G[i]
    pivot, pivot_i = findPivot(row)

    if pivot == None:
        print("No pivot found")
        continue

    multiplyAndSubtract(pivot_i, i, reversed(range(0, i)))

    

print("Finale matrix für Gauss-Jordan")
print(G)