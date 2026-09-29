
#Functional Programming(Normal programming):
nums=[1,2,3,4,5]
result=[]
for num in nums:
    result.append(num*2)
print(result)

#1.Lambda function
'''A lambda is a small anonymous function.

Anonymous means function ki separate name undadu'''
nums=[1,2,3,4,5]
res=list(map(lambda x:x*2,nums))
print(res)

'''lambda → small function
map() → applies function to every element
list() → converts result into a list'''

#Example
def square(x):
    return x * x

print(square(5)) #This is normal Function

square = lambda x: x * x #lambda arguments: expression

print(square(5))#This is lambdafunction

#another example for lambda
res=lambda a,b:a+b
print(res(10,20))

#map()-> map() is used when we want to apply a function to every element.
#Prathi element meeda same operation apply cheyyali ante map() use chestham.#
numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

print(list(result))
 #Example without lambda
def double(x):
    return x*3
nums=[1,2,3,4,5]
res=map(double,nums)
print(list(res))

#filter() -> filter() is used to select elements based on a condition.
#Condition satisfy ayye elements matrame kavali ante filter() use chestham
nums=[1,2,3,4,5]
res=filter(lambda x:x%2==0,nums) #filter(function, iterable)
print(list(res)) 

'''map    → Modify
filter → Select'''


#reduce() -> reduce() is used to combine multiple values into one value.
from functools import reduce
nums=[1,2,3,4,5]
res=reduce(lambda a,b:a+b,nums)
print(res)

#ZIP() -> zip() is used to combine corresponding elements from two or more iterables.
names=["Aswini","Mounika","Janu","pavi"]
age=[22,23,20,21]
res=zip(names,age)
print(list(res))
#real world use
names = ["A", "B", "C"]
marks = [90, 80, 70]

for name, mark in zip(names, marks):
    print(name, mark)

#sorted() with lambda ,We can use lambda with sorted().
students=[
    ("Aswini",90),
    ("Mounika",95),
    ("janu",87),
    ("pavitra",93)
]
result=sorted(students,key=lambda x:x[1])
print(result)
#descending order(reverse order)
students=[
    ("Aswini",90),
    ("Mounika",95),
    ("janu",87),
    ("pavitra",93)
]
result=sorted(students,key=lambda x:x[1] ,reverse=True)
print(result)

#List Comprehension-> List comprehension is another important Python functional-style concept.
#normal function
numbers = [1, 2, 3, 4, 5]

squares = []

for x in numbers:
    squares.append(x * x)

#print(squares)
#List comprehension
numbers=[1,2,3,4,5]
squares=[x*x for x in numbers] #[x * x for x in numbers]
print(squares)

#List Comprehension with condition
nums=[1,2,3,4,5,6]
even=[x for x in nums if x%2==0]
print(even)

'''Higher-Order Functions
A function that takes another function as an argument, OR
returns another function is called a higher-order function.'''
def calculate(func,x): #lambda n: n * 2 is passed as an argument to calculate().
    return func(x)
result=calculate(lambda x:x*2,16)
print(result)
#map(), filter() are common examples of functions that accept another function

#Function Returning Another Function
def multiplier(n):
    return lambda x:x*n
res=multiplier(5)
print(res(10))

#Combaining map()+filter()
nums=[1,2,3,4,5]
result=map(lambda x:x*x,filter(lambda x:x%2==1,numbers))
print(list(result))


    
    



