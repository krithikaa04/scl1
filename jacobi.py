#Gauss jacobi

import numpy as np

def jacobi(A,B,x,n):
    D=np.diag(A)
    R=A-np.diagflat(D)
    for i in range(n):
        x=(B-np.dot(R,x))/D
        print(x)
    return x

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
     
print("\n\nAUGUMENTED MATRIX :\n")     
for i in a:
    print(i)
A = np.array(a)
b = np.array(b)
n=10
x = [0,0,0]
x = jacobi(A,b,x,n)

"""
print("a)")
A=np.array([[4,1,1],[1,5,2],[1,2,3]])
B=[2,-6,-4]
x=[0,0,0]
n=10
x=jacobi(A,B,x,n)

print("b)")
A=np.array([[2,5],[1,2]])
B=[21,8]
x=[0,0]
x=jacobi(A,B,x,n)

print("c)")
A=np.array([[2,3,-1],[3,2,1],[1,-5,1]])
B=[5,10,0]
x=[0,0,0]
x=jacobi(A,B,x,n)
"""