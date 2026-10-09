'''NumPy stands for Numerical Python. It is one of the most important Python libraries for numerical calculations, 
data analysis, and Machine Learning.

The main object in NumPy is called an array (ndarray).'''

'''
What is NumPy?
Normally, Python lists can store numbers:numbers = [10, 20, 30, 40, 50]
But when we work with a large amount of numerical data, NumPy arrays are much more useful.

import numpy as np
numbers = np.array([10, 20, 30, 40, 50])

Here:
np → commonly used short name for NumPy
np.array() → creates a NumPy array
numbers → NumPy array
'''

'''
Why do we use NumPy?

NumPy provides:
Fast numerical calculations
Arrays and multidimensional arrays
Mathematical functions
Statistical functions
Matrix operations
Linear algebra
Random number generation
Functions useful for Machine Learning
'''

#import numpy as np
#print(np.__version__)

#1D Array,A one-dimensional array is similar to a Python list.
import numpy as np
arr1 = np.array([10, 20, 30, 40, 50])
print(arr1)
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)

#arr.ndim -> Dimensions of an Array
import numpy as np
ar=np.array([10,22,33,45])
print(ar.ndim)# 1 Dimensional array

import numpy as np
a1=np.array([[10,22,33,45],[11,23,56,68]])
print(a1.ndim)#2 Dimensional array

#Shape->shape tells us the size of each dimension.
import numpy as np
ar1=np.array([10,22,33,45])
print(ar1.shape)

import numpy as np
ar2=np.array([[10,22,33,45],[11,22,33,45]])
print(ar2.shape)

#Size -> size tells us the total number of elements.

arr3= np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr3.size)

#Data Type — dtype tells us what type of data is stored in the array.
arr4 = np.array([10, 20, 30])
print(arr4.dtype)
arr5 = np.array([7.88,5.66,8.99])
print(arr5.dtype)

'''Python List vs NumPy Array
Python List
a = [1, 2, 3]
NumPy Array
a = np.array([1, 2, 3])

One major difference is numerical operations.
With NumPy:
a = np.array([1, 2, 3])
print(a * 2)
Output:
[2 4 6]
Every element is multiplied by 2.'''


#Basic Array Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b) #Addition
print(a-b) #Subtraction
print(a*b)#Multiplication
print(a/b)#division

#Scalar Operations -> A scalar means a single number.
a2 = np.array([10, 20, 30])
print(a2 * 2) #Multiply by 2
print(a2 + 5) #Added by 5
print(a2 - 5) # Subtraction -> This is called vectorized operation.

#Indexing -> NumPy indexing starts from 0.
arr6 = np.array([10, 20, 30, 40, 50])
print(arr6[0])
print(arr6[2])
#Negative Indexing -> You can access elements from the end.
arr7 = np.array([10, 20, 30, 40, 50])
print(arr7[-1])
#2D Array Indexing
arr8 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr8[0, 0])#Access 10:


#Slicing -> Slicing means selecting a portion of an array.
arr9 = np.array([10, 20, 30, 40, 50])
print(arr9[1:4])

#np.zeros(),Creates an array containing zeros.
arr0 = np.zeros(5)
print(arr0)

#np.ones(),Creates an array containing ones.
arr11 = np.ones(5)
print(arr11)

#np.full(),Creates an array with the same specified value.
arr12 = np.full(5, 7)
print(arr12)
arr13 = np.full((2, 3), 5)
print(arr13)

#np.linspace() -> linspace() creates a specified number of equally spaced values.
arr13 = np.linspace(0, 10, 5)
print(arr13)

'''
Difference
np.arange()is mainly based on step size.
np.linspace()is mainly based on number of values.'''

#Reshape -> reshape() changes the shape without changing the data.
arr14 = np.array([1, 2, 3, 4, 5, 6])
new_arr = arr14.reshape(2, 3)
print(new_arr)

#Flatten -> flatten() converts a multidimensional array into a 1D array.
arr15 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

result = arr15.flatten()

print(result)

#Transpose -> Transpose changes rows into columns and columns into rows.
arr16 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr16.T)

#Important Mathematical Functions
#NumPy provides many mathematical functions.
array = np.array([4, 9, 16])
print(np.sqrt(array))
print(np.power(array, 2))
print(np.sum(array))
print(np.mean(array))
print(np.median(array))
print(np.min(array))
print(np.max(array))
print(np.var(array))
print(np.std(array))
print(np.argmin(array))
print(np.argmax(array))
print(np.sort(array))
arr20 = np.array([-10, -5, 2, 8])
print(np.abs(arr20))


'''Important NumPy Functions — Quick Revision
Function	Purpose
np.array()	Create array
np.zeros()	Create zeros
np.ones()	Create ones
np.full()	Create array with specified value
np.arange()	Create sequence using step
np.linspace()	Create equally spaced values
np.reshape()	Change shape
np.flatten()	Convert to 1D
.ndim	Number of dimensions
.shape	Dimensions/shape
.size	Number of elements
.dtype	Data type
np.sum()	Sum
np.mean()	Average
np.median()	Median
np.min()	Minimum
np.max()	Maximum
np.std()	Standard deviation
np.var()	Variance
np.sort()	Sort values
np.argmin()	Index of minimum
np.argmax()	Index of maximum
np.sqrt()	Square root
np.abs()	Absolute value
np.power()	Power
np.where()	Conditional selection
np.concatenate()	Join arrays
np.vstack()	Vertical stack
np.hstack()	Horizontal stack
np.dot()	Dot product
np.matmul()	Matrix multiplication
np.random.rand()	Random decimal values
np.random.randint()	Random integers'''

import numpy as np

# Create an array
marks = np.array([70, 80, 65, 90, 85])

# Basic information
print("Array:", marks)
print("Dimension:", marks.ndim)
print("Shape:", marks.shape)
print("Size:", marks.size)
print("Data type:", marks.dtype)

# Statistics
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Standard Deviation:", np.std(marks))

# Sorting
print("Sorted:", np.sort(marks))

# Filtering
print("Marks greater than 75:", marks[marks > 75])
