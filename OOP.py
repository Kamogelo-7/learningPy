# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects

username = str(input("what is your name?"))
userage = int(input("what is your age?"))
enrollmentYear = int(input("What year did you enroll?"))

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

# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Student(Person):
    def __init__(self, name, age, enrolled):
        super().__init__(name, age)
        self.enrolled = enrolled

    def enrolledYear (self):
        return f"Hello {self.name} you have enrolled in this colleage since {self.enrolled}"

Student1 = Student(username, userage , enrollmentYear)
print(Student1.enrolledYear())

