#Linear Algebra(numbers ni vectors and matrices form lo organize chesi, calculations cheyyadam)
'''Linear Algebra is a branch of mathematics that deals mainly with:

Numbers
Scalar
Vectors
Matrices
Linear equations
Transformations'''

#Scalar(A scalar is a single number.)
#Example : x = 10
#Single value/number ni scalar antaru.
'''v = [2, 4, 6]'''
import numpy as np
v=np.array([2,4,6])
print(v)

#Scalar Multiplication (We can multiply a vector by a scalar.)
A=np.array([5,3,9,7])
print(4*A)






#Vector -> (A vector is an ordered collection of numbers.)
'''Vectors can represent multiple properties together.
For example, a student:

[age, marks, attendance]

#Scalar → one number

#Vector → collection of numbers
'''



'''Dimension of a Vector
The number of elements in a vector is its dimension.
Example:[2,5] has 2 dimensions.
[10]              → 1D
[10,20]           → 2D
[10,20,30]        → 3D
[10,20,30,40]     → 4D'''

#Vector Addition
import numpy as np
res1=np.array([2,4,6,8])
res2=np.array([1,3,5,7])
print(res1+res2)

#Vector Subtraction
import numpy as np
A=np.array([6,7,8,9])
B=np.array([2,5,3,2])
print(A-B)

#Vector Multiplication
import numpy as np
A=np.array([2,3,4,5])
B=np.array([9,7,5,3])
print(A*B)


#Vector Magnitude(The magnitude tells us the length/size of a vector.)
'''For Example: v=[3,4] 

Magnitude:
           v=
'''
import numpy as np
v=np.array([3,4])
magnitude=np.linalg.norm(v)
print(int(magnitude))

'''Unit Vector->A unit vector has magnitude 1.'''
v=np.array([3,4])
unit_vector=v/np.linalg.norm(v)
print(unit_vector)
'''
#Vector → direction + magnitude
#Unit vector → same direction, magnitude = 1'''

#Dot Product

'''Suppose:
$$ A=[1,2,3] $$ $$ B=[4,5,6] $$
Dot product:
$$ A\cdot B $$
Multiply corresponding elements and add:
$$ (1×4)+(2×5)+(3×6) $$ $$ =4+10+18 $$ $$ =32 $$'''

a=np.array([1,2,3])
b=np.array([4,5,6])
result=np.dot(A,B)
print(result)


#Matrix(A matrix is a rectangular arrangement of numbers in rows and columns.)
A=np.array([[1,2,3],[4,5,6]])
print(A)
print(A.shape)#(Rows and columns lo numbers arrange chesina structure ni matrix antaru.)

'''x=[22 85 90
   20 96 95
   21 90 88]'''
#Rows    → students/data points
#Columns → features

#Matrix Operations

#1.Matrix addition
A=np.array([[1,2],[3,4]])
B=np.array([[6,7],[8,9]])
print(A+B)

#2.Matrix multiplication(Matrix multiplication is different from normal element-by-element multiplication.)
A=np.array([[1,2],
            [5,6]])
B=np.array([[4,5],
            [3,4]])
print(A @ B) #The @ operator is commonly used in Python for matrix multiplication.

#Matrix Transpose
'''
Transpose means:

Rows become columns and columns become rows.
Example:
 
     A=[1 2 3
        4 5 6] becomes

    Transpose
   A  =[1 4
        2 5
        3 6]
'''
A=np.array([[1,2,3],
            [4,5,6]])
print(A.T)

#Tensor(A tensor is a multi-dimensional data structure used to represent and process numerical data.)
'''Now we come to Tensor.

A tensor is a generalized multi-dimensional array.

Think of it like this:

Scalar → 0 dimensions
Vector → 1 dimension
Matrix → 2 dimensions
Tensor → 3+ dimensions

Example:
[
    [
        [1, 2],
        [3, 4]
    ],

    [
        [5, 6],
        [7, 8]
    ]
]
'''
A=np.array([
            [[1,2],[3,4]],
            [[5,6],[3,5]]
            ])
print(A.shape)



#NumPy Example — All Four
#import numpy as np

# Scalar
scalar = np.array(5)

# Vector
vector = np.array([1, 2, 3])

# Matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Tensor
tensor = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(scalar.ndim) #.ndim tells number of dimensions
print(vector.ndim)
print(matrix.ndim)
print(tensor.ndim)
'''Scalar → one value
Vector → list of values
Matrix → table of values
Tensor → collection of matrices / N-dimensional data'''

'''4Dimensional Tensor'''
import numpy as np

tensor = np.zeros((5, 2, 3, 4))# 5 groups,2 metrices,3 rows,4 columns

print(tensor.shape)
print(tensor.ndim)
print(tensor.size)