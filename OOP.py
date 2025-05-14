# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects

username = str(input("what is your name?"))
userage = int(input("what is your age?"))

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def user (self):
        print(f"Hello {self.name} you are {self.age} years old.")

    def checkUserAge (self):
        if(userage < 18):
            print(f"hello {self.name} i can't allow you to enter your to young {self.age} ")

user1 = Person(username, userage)
user1.user()
user1.checkUserAge()
