#RREF and REF (with and without library)
import sympy
from sympy import *
def getRank(mat):
    rank=0
    for i in mat:
        temp=0
        for j in range(len(i)):
            if(i[j]==0):
                temp+=1
        if(temp==len(i)):
            rank+=1
    return(len(mat)-rank)
        
def subRows(l1,l2,key):
    ans=[]
    for i in range(len(l1)):

        ans.append(l1[i]-(key*l2[i]))
        
    return ans
def Print(mat):
    print()
    for i in mat:
        print(i)
def getRREF(mat):                               #To get RREF of the Matrix
    mat.reverse()
    for i in mat:
        if(1 in i):
            ones=i.index(1)
        else:
            continue
        ind=mat.index(i)
        for j in range(ind,len(mat)-1):
            key=mat[j+1][ones]
            mat[j+1]=subRows(mat[j+1],mat[ind], key)
    mat.reverse()
    return mat
def getRowEcholon(mat):                         #To get REF of the matrix
    ptr=0
    for i in mat:
        div=i[ptr]
        if(div!=0):
                for k in range(ptr,len(i)):
                    i[k]=i[k]/div
        ind=mat.index(i)
        for j in range(ind,len(mat)-1):
            key=mat[j+1][ptr]
            mat[j+1]=subRows(mat[j+1],mat[ind],key)
        ptr+=1
    return mat
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
REF=getRowEcholon(mat)
rank=getRank(REF)
RREF=getRREF(REF)
print("\n\nRREF and REF WITHOUT using library")
print("RREF of the matrix : ")
Print(RREF)
print("Rank of the matrix : ",rank)    

print("\n\nRREF and REF WITH using library")
M = Matrix(mat)
M_rref = M.rref()
print("The Row echelon form of matrix M and the pivot columns : {}\n".format(M_rref))  

