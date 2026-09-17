'''Dunder Methods
    Dunder means Double Underscore.

Dunder = Double Underscore
They start and end with two underscores.

They are also called Magic Methods or Special Methods.
'''

'''
__init__
__str__
__len__
__add__
__eq__
'''
#__init__() —> Constructor(__init__() is called automatically when we create an object.)
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
stu=Student("Aswini",22)
print(stu.name)
print(stu.age)

# __str__() — > Object ni String ga Represent Cheyyadam(Normally, printing an object gives something like an object address.

#Instead, we can define __str__().)
class Student:
    def __init__(self,name,bgroup):
        self.name=name
        self.bgroup=bgroup
    def __str__(self):
        return f"Name : {self.name},Bloodgroup : {self.bgroup}"
std=Student("Ashu","O positive")
print(std)

#__len__() —> len() Function (If we want len(object) to work, we can define __len__().)
class Students:
    def __init__(self,players):
        self.players=players
    def __len__(self):
        return len(self.players)
std=Students(['A','B','C','D',1])
print(len(std))

#__add__() —> + Operator (We can define how + should behave for our objects.)
class Number:
    def __init__(self,value):
        self.value=value
    def __add__(self, other):
        return self.value+other.value
a=Number(30)
b=Number(25)
print(a+b)

#__eq__() —> == Operator (eq__() defines how two objects should be compared using ==.)
class Fruits:
    def __init__(self,name):
        self.name=name
    def __eq__(self, other):
        return self.name==other.name
f1=Fruits("Apple")
f2=Fruits("Apple")
print(f1==f2)

#__lt__() — < _lt__ means less than.(example 5<10)
class Number:
    def __init__(self,value):
        self.value=value
    def __lt__(self, other):
        return self.value < other.value
n1=Number(10)
n2=Number(25)
print(n1<n2)

#__gt__() — >__gt__ means greater than.(Example 50>10)
class Number:
    def __init__(self,value):
        self.value=value
    def __gt__(self, other):
        return self.value > other.value
n1=Number(100)
n2=Number(25)
print(n1>n2)

#__getitem__() —> [] It allows an object to work with indexing.
class Fruits:
    def __init__(self,names):
        self.names=names
    def __getitem__(self, key):
        return self.names[key]
fr=Fruits(["appple","banana","grapes","guava","mango"])
print(fr[2])

#__setitem__() — Assigning Using [] We can also control:(object[index] = value)
class Fruits:
    def __init__(self,names):
        self.names=names
    def __setitem__(self, key,value):
        self.names[key]=value
fr=Fruits(["appple","banana","grapes","guava","mango"])
fr[2]="sapota"
print(fr.names)

#__contains__() — in (value in object)
class MyList:
    def __init__(self, items):
        self.items = items

    def __contains__(self, value):
        return value in self.items


numbers = MyList([10, 20, 30])

print(20 in numbers)


#__iter__() — Iteration (like for loop)

class MyNumbers:
    def __init__(self):
        self.numbers = [10, 20, 30]

    def __iter__(self):
        return iter(self.numbers)


obj = MyNumbers()

for number in obj:
    print(number)

#Using __repr__() -> We can define our own representation:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"


student = Student("Aswini", 23)

print(student)

#__new__() — Creating an Object (__new__() is related to object creation.)
#__new__()  → creates the object
#__init__() → initializes the object

class Student:
    def __new__(cls, name):
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self, name):
        print("__init__ called")
        self.name = name


student = Student("Aswini")
print(student.name)

#__del__() — Object Cleanup (__del__() is called when an object is being finalized.)
class Student:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Object is being deleted")


student = Student("Aswini")
del student

#__call__() — Object Behaves Like a Function
class Greeting:
    def __call__(self):
        print("Hello Aswini")


greet = Greeting()

greet()


#__hash__() — Hash Value
#This is especially relevant to your HashMap/dictionary topic.

#__hash__() returns a hash value for an object when the object is hashable.
class Student:
    def __init__(self, roll_no):
        self.roll_no = roll_no

    def __hash__(self):
        return hash(self.roll_no)
student = Student(101)

print(hash(student))

#__bool__() — True or False(__bool__() controls what happens when an object is used in a Boolean context.)
#if object:
#    print("True")
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __bool__(self):
        return self.marks > 40


student1 = Student(60)

if student1:
    print("Pass")