'''Encapsulation

Encapsulation = Combining data and methods inside a class and controlling access to the data.'''
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)

print(account.get_balance())

'''Inheritance

Inheritance means one class can acquire properties and methods from another class.'''
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()

'''Polymorphism

Polymorphism = One interface/name can have different behavior depending on the object.'''
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

#Method Overriding
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()

'''
Abstraction

Abstraction means hiding implementation details and showing only the required functionality.
'''
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()