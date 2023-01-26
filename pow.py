#POWER METHOD and INVERSE Power

def Print(mat):
    print()
    for i in mat:
        print(i)
import numpy as np
import sympy as sp
def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n
def power(A,iter):
  b=np.array([1,1,1])
  for i in range(iter):
    b=np.dot(A,b)
    b_l,b=normalize(b)
  print('Eigenvalue:', b_l)
  print('Eigenvector:', b)
""" 
r1=[]
r2=[]
r3=[]

r1=[eval(i) for i in input("Enter row 1 elements separated by space").split(" ")]
r2=[eval(i) for i in input("Enter row 2 elements separated by space").split(" ")]
r3=[eval(i) for i in input("Enter row 3 elements separated by space").split(" ")]
"""
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
mat=np.array(mat)
print(power(mat,10))
print(power(np.linalg.inv(mat),10))#inverse power method