import numpy as np
def checkLow_tringle(mat):          #this will check for any zero rows , to make it as a trailing row
    for i in range(3):
        if(((mat[i][0]==0) & (mat[i][1]==0)) & (mat[i][2]==0)):
            lst=mat[i]
            mat.pop(i)
            mat.append(lst)
    return mat
            
def evaluate(mat):                  # for calculating eigen vector after compting RREF of (A- (lamda)*I)
    eigVec=[0,0,0]                  
    for i in range(3):
        if(((mat[i][0]==0) & (mat[i][1]==0)) & (mat[i][2]==0)):
            eigVec[i]=1
    if(eigVec[0]==0):
        x=-mat[0][1]-mat[0][2]
        eigVec[0]=x
    if(eigVec[1]==0):
        y=-mat[1][0]-mat[1][2]

        eigVec[1]=y
    if(eigVec[2]==0):
        z=-mat[2][0]-mat[2][1]
        eigVec[2]=z
    return eigVec
        
def subRows(l1,l2,key):                         # Subracting two rows for row elementary operations
    ans=[]
    for i in range(len(l1)):

        ans.append(l1[i]-(key*l2[i]))
        
    return ans
def getRREF(mat):                               #To get RREF of the Matrix
    mat.reverse()                               #this will compute RREF for a REF matrix
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
 
    return (mat)

def getRowEcholon(mat):                         #To get REF of the matrix
    ptr=0                                       
    mat=checkLow_tringle(mat)
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
        mat=checkLow_tringle(mat)
    return mat
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def Trace(matrix,n):
    trace = 0                           # To get trace of a matrix
    for i in range(0,n):
        for j in range(0,n):
            if i == j:
                trace += matrix[i][j]
            else:
                continue
    return trace
def Sum(matrix,n):
    Sum = 0                         # to get  Sum of all minors of the matrix
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                temp = getMatrixMinor(matrix,i,j)
                Sum += temp[0][0]*temp[1][1] - temp[0][1]*temp[1][0]
    return Sum
def AminusLamdaI(A,lam):
    I=[[1,0,0],[0,1,0],[0,0,1]]
    for i in range(3):                  # Computes (A - (lamda)*I) and return RREF of the resultant matrix
        I[i][i]=int(lam)
    res=[]
    for i in range(3):
        lst=[]
        for j in range(3):
            lst.append(A[i][j]-I[i][j])
        res.append(lst)
    result=getRREF(getRowEcholon(res))
    result=evaluate(result)
    return result
def getPmatrix(mat):
    lst=[[0,0,0],[0,0,0],[0,0,0]]       
    for i in range(3):
        for j in range(3):
            lst[j][i]=mat[i][j]
    return lst

mat=[]

for i in range(0,3):				#GIVE THE INPUT IN THE NORMAL INPUT FORMAT
     temp = []
     for j in range(0,3):
         ele = float(input("Enter a[" + str(i+1) + "][" + str(j+1) + "] :"))
         temp.append(ele)
     mat.append(temp)
Det = np.linalg.det(mat)
trace=Trace(mat,len(mat))
Sum=Sum(mat,len(mat))
a=1
exp = [a,-1*trace,Sum,-1*Det]
sol = np.roots(exp)
EigValues=[]
for i in sol:
    EigValues.append(np.round(i,0))
EigVec=[]
print("Eigen values of the given matrix :",EigValues)
for i in EigValues:
    EigVec.append(AminusLamdaI(mat,i))
print("Eigen Vectors of the given matrix : ")
print(EigVec)
P=np.array(getPmatrix(EigVec))
Pinv=np.linalg.inv(P)
#print(P)
#print(Pinv)
temp=np.dot(Pinv,mat)
res=np.dot(temp,P)
print("Diagonal matrix using P^-1 * D * P method : ")
print(res)
print("Diagonal matrix : ")
for i in range(3):
    for j in range(3):
        if(i==j):
            print(EigValues[i]," ",end=" ")
        else:
            print(0,"  ",end=" ")
    print()

