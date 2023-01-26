import numpy as np
import sympy as sp
def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1 :] for row in ( m[:i] + m[i+1:]) ]
def det(mat):
    mat[0]
def Trace(matrix, n):
    trace = 0
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                trace += matrix[i][j]
            else:
                continue
    return trace
def Sum(matrix, n):
    Sum = 0
    for i in range(0, n):
        for j in range(0, n):
            if i==j:
                temp = getMatrixMinor(matrix, i, j)
                Sum += temp[0][0] * temp[1][1] - temp[0][1] * temp[1][0]
    return 
def determinant(mat):
    x=mat[0][0]*(mat[1][1]*mat[2][2]- mat[1][2]*mat[2][1])
    y=mat[0][1]*(mat[1][0]*mat[2][2]- mat[1][2]*mat[2][0])
    z=mat[0][2]*(mat[1][0]*mat[2][1]- mat[1][1]*mat[2][0])
    return x-y+z
def EigenValues(mat):
    Det   = determinant(mat)
    trace = Trace(mat,len(mat))
    sm = Sum(mat,len(mat))
    a = 1
    exp = [a, -1 * trace, sm, -1 * Det ]
    sol = np.roots(exp)
    EigValues = []
    for i in sol:
          EigValues.append(np.round(i,0))
    return EigValues

x = sp.var('x')
y = sp.var('y')
z = sp.var('z')

n = int(input("Enter no. of variables : "))
expr = sp.sympify(input("Enter the Quadratic form (a*x**2+b*y**2+c*z**2-d*x*y...): "))

symmetric_matrix = [ [] for  i in  range(n) ]
symmetric_matrix[0].append( expr.coeff(x**2) )
symmetric_matrix[0].append( int( 0.5 * (expr.coeff( x * y ))) )
symmetric_matrix[0].append( int( 0.5 * (expr.coeff( x * z ))) )
symmetric_matrix[1].append( int( 0.5 * (expr.coeff( x * y ))) )
symmetric_matrix[1].append( expr.coeff( y**2 ) )
symmetric_matrix[1].append( int( 0.5 * (expr.coeff( y * z ))) )
symmetric_matrix[2].append( int( 0.5 * (expr.coeff( x * z ))) )
symmetric_matrix[2].append( int( 0.5 * (expr.coeff( y * z ))) )
symmetric_matrix[2].append( expr.coeff( z**2 ) )
        
print("\nSymmetric matrix for given Quadratic form is : ", symmetric_matrix )

matrix = EigenValues( list(symmetric_matrix) )

print("\nCanonical form for given Quadratic form is : ")
print("{}x2+{}*y2+{}*z*2".format(matrix[0], matrix[1], matrix[2] ), end = "\n\n")

#wit fucntions
def Cannonical(A):
    #A is a matrix
    A = sp.Matrix(A)
    P,D = A.diagonalize()
    return D

A = np.array([[4.0,0,1.0],[-2.0,1.0,0],[-2.0,0,1.0]])
d = Cannonical(A)

print(d)