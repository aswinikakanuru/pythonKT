class Student:
    name = "Aswini"
    age = 23
student1 = Student()
print(student1.name)
print(student1.age)

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

student1 = Student("Aswini", 23)

student1.display()