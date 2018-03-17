# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:13:43 2018

@author: Michele97
"""


#test: A = A=[[-2.0, -1.0, 2.0], [0.0, -1.0, 2.0], [1.0, 2.0, -2.0], [2.0, -2.0, -2.0]]
#      b =[0.0, 0.0, 0.0, 0.0]



from scipy import *
from numpy import *


def scalini(A,b):
    A = copy(A)
    b = copy(b)
    [m, n] = shape(A);

    tol = 1e-15
    pos_piv = -1
    for i in range (0, m - 1):   
        piv_nullo = True
        s = 1
        while piv_nullo and pos_piv + s < n:
            if A[i, pos_piv + s] == 0:    
                tecnicaMaxPivot(A, b, i, pos_piv)
                s = s + 1
            else:
                piv_nullo = False
                pos_piv = pos_piv + s
                pivot = A[i, pos_piv]
            
        if not(piv_nullo):
            for r in range (i + 1, m):
                mol = (-1) * (A[r, pos_piv] / pivot)
                
                b[r] = (mol * b[i]) + b[r]
                
                for c in range (0, n):
                    A[r,c] = (mol * A[i,c]) + A[r,c]
                    
            print ("                ")
    return A, b
        
 
    
    
def tecnicaMaxPivot(A, b, i, pos_piv):
    esito = False
    [m, n] = shape(A)
    r =  i + 1
    while r < m and not(esito):
        c = pos_piv + 1
        if A[r, c] != 0:
            esito = True
            swapRighe(A, b, r, i)
        r = r + 1
        
        
        
def swapRighe(A, b, r, i):
    [m, n] = shape(A)
    for j in range (0, n):
        temp = A[i, j]
        A[i, j] = A[r, j]
        A[r, j] = temp
        
    temp = b[r]
    b[r] = b[i]
    b[i] = temp
    
    