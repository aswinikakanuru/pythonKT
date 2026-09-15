'''List 
Lists maintain the order in which elements are inserted.
List is Mututable.Mutable means we can change the list after creating it.
A list can contain different types of data.
List indexing starts from 0.Negative indexing is also possible
List allows Duplicates'''

#List methods are append(),insert(),remove(),pop(),len(),sort(),reverse(),extend(),clear(),Copy(),

skills=["Java","Python","Springboot","sql","java",23]
skills[2]="Javascript"
skills.append("React")
skills.insert(5,"MongoDB")
skills.remove("java")
print(len(skills))
skills.pop()


for i in skills:   
    print(i)
print(skills[-3]) #Negative indexing
print(len(skills))

#User Inputs for strings
skills = input("Enter your skills: ").split()

print(skills)

#User Inputs for integers
numbers = list(map(int, input("Enter numbers: ").split()))

print(numbers)

#Another Example

#sort()
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

#Descending Order
numbers.sort(reverse=True)

print(numbers)

#reverse()
skills = ["Java", "Python", "SQL", "React"]

skills.reverse()

print(skills)

#sort()     → arranges elements
#reverse()  → reverses current order

#extend()
skills = ["Java", "Python"]

skills.extend(["SQL", "React"])

print(skills)

#append() → adds one item
#extend() → adds multiple items

#clear()
numbers = [10, 20, 30]

numbers.clear()

print(numbers)

#copy()
skills = ["Java", "Python", "SQL"]

new_skills = skills.copy()

print(new_skills)

#Nested Lists -> A list can contain another list.
students = [
    ["Aswini", 23],
    ["Ravi", 24],
    ["Anu", 22]
]

print(students)
print(students[0][0])