# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:05:29 2022
@author: denni
"""
print("\n--------- Aufgabe 3 ---------")
# Python initialisieren :
import numpy as np
#Parameter
#a entspricht der linken Seite vom Gauss Schema, den Gleichungen
a = [[3,-2,5,0],
    [4,5,8,1],
    [1,1,2,1],
    [2,7,6,5]]
#b entspricht der rechten Seite vom Gauss Schema, den Lösungen
b = [2,4,5,7]
#Funktion
def LGLS_Gauss(a,b):
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)
    x = np.zeros(n, float)
    #Auslöschung pro zeile --> in der Diagonale die Nullen einsetzen
    #Funktion läuft von der ersten Zeile 1 bis zur vorletzten Zeile n-1
    for k in range(n-1):
        #i ist der Index für Zeilen unter den bereits berechneten Zeilen
        #Funktion läuft von der zweiten Zeile k+1  bis zur letzten Zeile n
        for i in range(k+1, n):
            #falls der Wert bereits 0 ist wird zur nächsten Zeile gewechselt
            if a[i, k] == 0: continue
            factor = a[k, k]/a[i, k]
            #j ist der Index für die Spalte
            #Funktion läuft jeweils mit der bereits berechneten Zeile k bis n
            for j in range(k, n):
                #Berechnung der Auslöschung
                a[i, j] = a[k, j] - a[i, j]*factor
            #Berechnung der Auslöschung für die Lösungswerte (rechte Seite vom Gauss Schema)
            b[i] = b[k] - b[i]*factor
    
    #Rückwärts einsetzen der Werte
    #Loop geht rückwärts, daher entsprechend die Werte für die Schlaufe verringern
    x[n-1] = b[n-1] / a[n-1, n-1]
    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += a[i, j] * x[j]
        x[i] = (b[i] - sum_ax) / a[i, i]
    return b, a, x
def LGLS_GaussJordan(a, b, tol=-1):
    '''
    Beim Gauss Jordan wird pro Spalte die Werte bereits für die Auslöschung berechnet
    Sprich es wird jeweils auf 0 gesetzt mit Hilfe der Auslöschung gemäss Gauss
    '''
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)
    G = np.c_[a, b]
    if tol < 0:
        tol = np.max(G.shape)*np.linalg.norm(G,ord=np.inf)*np.finfo(np.float64).eps
    #print(tol)
    for k in range(n):
        #partielles Pivotieren
        if np.fabs(a[k, k-1]) < tol:
            for i in range(k+1, n):
                if np.fabs(a[i, k]) > np.fabs(a[k, k]):
                    for j in range(k, n):
                       a[k, j], a[i, j] = a[i, j], a[k, j]
                    b[k], b[i] = b[i], b[k]
                    break
        #Divison Pivot Zeile
        pivot = a[k, k]
        for j in range(k, len(a[k])):
            print(a[k,j])
            a[k, j] /= pivot
        b[k] /= pivot
        #Auschlöschung Loop
        for i in range(n):
            if i == k or a[i, k] == 0: continue
            factor = a[i, k]
            for j in range(k, len(a[k])):
                a[i, j] -= factor * a[k, j]
            b[i] -= factor * b[k]        
    return b, a
X, A, sol = LGLS_Gauss(a, b)
print(f"Ergebnisse Matrix b LGLS:\n {X}")
print(f"Matrix A Gauss:\n {A}")
print(f"Lösung LGLS --> x Werte:\n {sol}")
print('\n-----------------------------\n')
print("\n--------- Aufgabe 5 ---------")
#Parameter:
a = [[2, 1, 0, 2],
    [4, 2, 3, 3],
    [-2, -1, 6, -4],
    [-8, -4, 9, -11],
    [2, 1, -3, 3]]
b = [6, 16, 2, -12, 2]
# a = [[0,2,0,1], [2,2,3,2], [4,-3,0,1], [6,1,-6,-5]]
# b = [0,-2,-7,6]
X, A = LGLS_GaussJordan(a, b)
print(f"Lösung LGLS --> x Werte:\n {X}")
print(f"Matrix A Gauss Jordan:\n {A}")