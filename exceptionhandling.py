#EXCEPTION HANDLING
'''An exception is an error that occurs while a Python program is running.'''

'''a=10
b=0
print(a/b)'''

try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Cannot divided by zero")
'''
#Multiple errors
try:
    number1=int(input("Enter your Number1:"))
    number2=int(input("Enter your Number2:"))
    result=int(number1/number2)
    
except ValueError:
    print("Enter Correct Input")
except ZeroDivisionError:
    print("cannot divided by zero")
else:
    print(result)'''

#finally   -->  finally executes whether an exception occurs or not.
try:
    print(10 / 2)

except ZeroDivisionError:
    print("Error")

finally:
    print("This always executes")

#raise --> raise is used when we want to manually generate an exception.
age=int(input("Enter your age:"))
if age<18:
    raise ValueError("Age is must be 18 or above 18 years")
else:
    print("Eligible,You can vote")


 #Custom Exception --> We can create our own exception class.   

'''class AgeError(Exception):
    pass


age = 15

if age < 18:
    raise AgeError("Age must be 18 or above")'''

'''Exception	Example
ValueError	int("abc")
TypeError	"10" + 5
ZeroDivisionError	10 / 0
IndexError	list[10] when index doesn't exist
KeyError	Missing dictionary key
FileNotFoundError	Opening a nonexistent file
NameError	Using an undefined variable
AttributeError	Accessing a nonexistent attribute'''

try:
    with open("student.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")

finally:
    print("File operation completed")