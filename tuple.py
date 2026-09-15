''' A Tuple is also a collection of multiple values.tuple_name = (value1, value2, value3)
    Tuple is ordered.Tuples maintain insertion order.
    Tuple is Immutable.Immutable means we cannot change the tuple after creating it.
    Tuple allows Duplicate Values, Allows Different Data Types
    Tuple supports indexing,Supports Slicing,

    
'''

# Tuples have fewer methods because they are immutable.count(),index(),

names=("Aswini","Santhosh","Prasad","Varalakshmi","Aswini",26,9.08,True)
#names[1]="sumanth" not possible becoz its immutable

for i in names:
    print(i)
print(names[2]) #indexing
print(names[1:3]) #Supports Slicing
print(names.count("Aswini"))
print(names.index("Santhosh"))

#user inputs
skills = tuple(input("Enter your skills: ").split())

print(skills)
#user inputs for integers
numbers = tuple(map(int, input("Enter numbers: ").split()))

print(numbers)