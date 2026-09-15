''' A Set is a collection of unique elements.
    set_name = {value1, value2, value3}
    Set does NOT allow duplicates,This is the most important property of a Set.
    Set is Mutable,We can add or remove elements after creating a set.
    Set is Unordered,A Set does not maintain a reliable insertion order.
    Set Does Not Support Indexing.
    A Set can contain different data types.

'''

# Set have fewer methods like add(),update(),remove(),discard(),pop()

numbers={10,20,30,40,50,"Aswini",8.9,"True"}
numbers.add(80)
numbers.remove(50)
numbers.update([101,102])
numbers.pop() #Removes an element from the set.Since a Set is unordered, you should not assume which element will be removed.
numbers.discard(8.9)#Discard also removes element,
                    # but the difference between remove and discard is this:
                    # remove()   → gives error if element doesn't exist
                    # discard()  → does not give error'''

#print(numbers[2])type error:set object is not subscriptable
print(numbers)
for i in numbers:
    print(i)




#Set operations
A={1,2,3,4}
B={3,4,5,6}
#Union  In both sets Unique Elements
print(A | B) # Union this is for unique elements
print(A.union(B))#this is for unique elements
 #Intersection : Returns elements that are present in both sets.
print(A & B)
print(A.intersection(B))
#Difference
print(A - B) #Returns elements that are in A but not in B.
print(B - A) #Returns elements that are in B but not in A.
#Symmetric Difference
print(A^B) #Returns elements that are in either set, but not in both.

#issubset()
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B)) # output is true or false

#issuperset()
A = {1, 2, 3, 4}
B = {1, 2}

print(A.issuperset(B))

#isdisjoint() //Checks whether two sets have no common elements.
A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))


a={} #This is NOT an empty Set.It is an empty Dictionary
print(type(a))

b=set()#This is an empty Set
print(type(b))

'''
#User Inputs
skills = set(input("Enter your skills: ").split())

print(skills)
#User Inputs for Integers
numbers = set(map(int, input("Enter numbers: ").split()))

print(numbers)'''
