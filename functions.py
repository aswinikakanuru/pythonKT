def greet():
    print("hello world")
greet()

def greet(name):
    print(name)
greet("Aswini")
#greet(input("Enter your name : "))

def students(name,age,id,dept):
    print("Name : ",name)
    print("Age : ",age)
    print("ID : ",id)
    print("Dept : ",dept)
students("Aswini",23,10198,"ECE")

def add(num1,num2):
    return num1+num2
result = add(10,20)
#result=add(int(input("Num1 : ")),int(input("Num2 : ")))
print(result)


def even_number(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
result=even_number(11)
print(result)

#default value parameter
def greet(name="Ashu"):
    print("Hello : ",name)
greet()

#keyword arguments
def greet(name,age):
    print("Name : ",name)
    print("Age : ",age)
greet(name="santhosh",age=20)

#*args allows us to pass multiple positional arguments to a function.
def add(*nums):
    print("Numbers -> ",nums)
add(10,20,30,40,50) #Inside the function, numbers is a tuple.

def addition(*nums):
    return sum(nums)
res=addition(10,20,30,40,50)
print(res)

#**kwargs allows us to pass multiple keyword arguments.
def student(**details):
    print(details)
student(name="sumanth",age=22,dept="ECE")#Inside the function, details is a dictionary.

def student(**details):
    for key, value in details.items():
        print(key, ":", value)

student(name="Aswini", age=23, course="B.Tech")


def test():
    x = 120 #local variable
    print("Local variable : ",x)

test()

x = 180 # global variable

def test():
    print("global Variable : ",x)

test()
