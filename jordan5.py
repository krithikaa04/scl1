# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:41:21 2023

@author: Krithika
"""

import numpy as np
n = int(input("Enter the number of equations :"))
m = int(input("Enter the number of variables  :"))

a = []
b = []

for i in range(0,n):
     print("\nEnter the equation " + str(i+1) + " :")
     temp = []
     for j in range(0,m+1):
         if j == m:
             con = int(input("Enter the constant :"))
             b.append(con)
         else:
             ele = int(input("Enter the co efcient of variable " + str(j+1) + " :"))
             temp.append(ele)
     a.append(temp)
A = np.array(a)
b = np.array(b)
x = np.linalg.solve(A, b)
print(x)