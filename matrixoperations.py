#Matrix Operations(A matrix is a rectangular arrangement of numbers in rows and columns.)
'''1.Matrix Addition'''
import numpy as np
A=np.array([[1,2],[3,4]])
B=np.array([[3,4],[5,6]])
print(A+B)

'''2.Matrix Subtraction'''
A=np.array([[3,7],[8,9]])
B=np.array([[1,4],[5,4]])
print(A-B)

'''3.Matrix Multiplication'''
A=np.array([[3,7],
            [8,9]])
B=np.array([[1,4],
            [5,4]])
print(A@B)


'''4.Scalar Multiplication'''
A=np.array([[3,7],
            [8,9]])
print(3*A)

'''Identity Matrix(An Identity Matrix is like the number 1 for matrix multiplication.)
For example:[1 0
             0 1] 2x2 matrix

             [1 0 0
              0 1 0
              0 0 1]3x3 matrix
'''
import numpy as np
I=np.eye(3) #Identity Matrix = Matrix version of number 1.
print(I)

'''Determinant(The determinant is a single number calculated from a square matrix.)
for 2x2 matrix is A=[a b
                     c d]
                det A=ad-bc  #this is important  
'''
import numpy as np
A=np.array([[2,3],
            [4,5]])
det=np.linalg.det(A)
print(det)
'''One important use is checking whether a matrix has an inverse.
       If determinant ≠ 0(The matrix is invertible.)
       If determinant = 0(The matrix is singular and does not have an inverse.)
       '''

'''A x A inverse=I (Identity matrix)
What does the inverse actually do?

Now multiply:

A × A⁻¹=I'''

#Inverse Matrix
import numpy as np
A=np.array([[2,3],
            [1,4]])
inverse=np.linalg.inv(A)
print(inverse)

'''Identity Matrix:
I = Matrix version of 1

Inverse:
A × A⁻¹ = I

Determinant:
det(A) = 0  → inverse doesn't exist
det(A) ≠ 0 → inverse exists'''
