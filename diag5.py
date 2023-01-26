#Diagonalize a matrix using library

import sympy 
from sympy import *
def Print(mat):
    print()
    for i in mat:
        print(i)
        
n = int(input("Enter the number of rows :"))
m = int(input("Enter te number of columns :"))

mat=[]

for i in range(0,n):				#GIVE THE INPUT IN THE NORMAL INPUT FORMAT
     temp = []
     for j in range(0,m):
         ele = int(input("Enter a[" + str(i+1) + "][" + str(j+1) + "] :"))
         temp.append(ele)
     mat.append(temp)
print("\nEntered matrix : ")
Print(mat)

M = Matrix(mat)
P, D = M.diagonalize()  
print("Diagonal of a matrix : \n{}".format(D))
