# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 21:30:06 2023

@author: Krithika
"""

def getRank(mat):
    mat =getRowEcholon(mat)
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
n = int(input("Enter the number of equations :"))
#m = int(input("Enter te number of columns :"))
unknowns=int(input("Enter the number of unknonws : "))
m = unknowns+1      #number of columns of matrix
matAB=[]
b=[]
for i in range(0,n):				#GIVE THE INPUT IN THE NORMAL INPUT FORMAT
     temp = []
     for j in range(0,unknowns+1):
        if j==unknowns:
             con = int(input("Enter the constant :"))
             b.append(con)
        else:
         ele = int(input("Enter the co efcient of variable " + str(j+1) + " :"))
         temp.append(ele)
     matAB.append(temp)
n= len(matAB[0])
matA=[]
for i in range(len(b)):
    matAB[i].append(b[i])
for i in matAB:
    matA.append(i[0:n])
Print(matA)
Print(matAB)
print(b)
print(matAB)

print("Entered matrix : ")
Print(matAB)
rankAB=getRank(matAB)
rankA=getRank(matA)
print("Rank of matrix [A:B] : ",rankAB)
print("Rank of matrix A : ",rankA,"\n")
if (rankAB==rankA):
    print("Consistent")
    if(rankAB ==unknowns):
        print("Unique Solutions : ")
        result=getRREF(getRowEcholon(matAB))
        Print(result)
        print("\n")
        for i in range(unknowns):
            print("Value of variable ",i+1," : ",result[i][-1])
    elif(rankAB<unknowns):
        print("Infinite solutions : ")
elif(rankA<rankAB):
    print("Inconsistent : No solutions")