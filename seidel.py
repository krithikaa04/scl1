#Gauss Seidel

import numpy as np

def seidel(a, b, sol):    
    n = len(a)                   
    for j in range(0, n):        
        d = b[j]                  
        for i in range(0, n):     
            if(j != i):
                d-=a[j][i] * sol[i]   
        sol[j] = d / a[j][j]          
    return sol

def diagonallyDominant(a, m):
    for i in range(len(a)):
        sum = 0
        for j in range(0,m):
            if i!=j:
                sum += abs(a[i][j])
        if a[i][i] >= sum :
            continue
        else:
            return False
    return True

n = int(input("Enter the number of equations :"))
m = int(input("Enter the number of variables  :"))

a = []
b = []
sol = np.zeros(n)

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
    
if diagonallyDominant(a,m) == True:  
   print("\nThe given matrix is diagonally dominant!\n SOLUTION :")
   for i in range(0,25):
      sol =  seidel(a, b, sol)
   print(sol)
   
else:
    print("\nThe given matrix is not diagonally dominant!")
    