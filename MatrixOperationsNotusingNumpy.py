#Matrix operations without using numpy
'''In normal Python, we represent a matrix using a list of lists.'''
A=[
    [1,2],
    [3,4]
]
print(A)

'''1. Matrix Addition

We add values at the same positions.'''
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
result=[[A[0][0]+B[0][0], A[0][1]+B[0][1]],
        [A[1][0]+B[1][0],A[1][1]+B[1][1]]]
print(result)

#Better way using loops
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
result=[]
for i in range(2):
    row=[]
    for j in range(2):
        row.append(A[i][j]+B[i][j])
    result.append(row)
print(result)

#3. Matrix Subtraction
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
result=[[A[0][0]-B[0][0], A[0][1]-B[0][1]],
        [A[1][0]-B[1][0],A[1][1]-B[1][1]]]
print(result)

#Better way using loops
B=[[1,2],[3,4]]
A=[[5,6],[7,8]]
result=[]
for i in range(2):
    row=[]
    for j in range(2):
        row.append(A[i][j]-B[i][j])
    result.append(row)
print(result)


#Scalar Multiplication
A=[[1,2],[3,4]]
scalar=2
result=[]
for i in range(2):
    row=[]
    for j in range(2):
        row.append(A[i][j]*3)
    result.append(row)
print(result)

#Element-wise Multiplication (Eaxmple=A*B ,means corresponding values multiply.)
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
result=[]
for i in range(2):
    row=[]
    for j in range(2):
        row.append(A[i][j]*B[i][j])
    result.append(row)
print(result)

#Matrix Multiplication(This is different from element-wise multiplication.)
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
result=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j]+=A[i][k]*B[k][j]
print(result)

#7. Transpose(Transpose means:Rows become columns.)
A=[[1,2,3],[4,5,6]]
result=[]
for j in range(3):
    row=[]
    for i in range(2):
        row.append(A[i][j])
    result.append(row)
print(result)


#Identity Matrix
n=3
identity=[]
for i in range(n):
    row=[]
    for j in range(n):
        if i==j:
            row.append(1)
        else:
            row.append(0)
    identity.append(row)
print(identity)
for i in identity:
    print(i)
#Matrix Determinant
A=[[2,3],
   [1,4]]
det=(A[0][0]*A[1][1])-(A[0][1]*A[1][0])
print(det)

#Matrix Inverse
A=[[2,3],
   [1,4]]
a=A[0][0]
b=A[0][1]
c=A[1][0]
d=A[1][1]
det=a*d-b*c
if det==0:
    print("Inverse doesnot exsist")
else:
    inverse=[[d/det,-b/det],
             [-c/det,a/det]]
print(inverse)