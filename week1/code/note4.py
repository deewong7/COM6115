"""
COM6115: Text Processing
Python Introductory Materials

Object Oriented Programming: Introduction, Defining Classes, Inheritance
"""

# bundles of data
class Person():
    # def __init__(self) -> None:
    #     self.firstname = None
    #     self.surname = None
    #     self.age = None
    #     self.species = 'Homo sapiens'

    def __init__(self, firstname = "", surname = "", age = "") -> None:
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.species = 'Homo sapiens'
    
    # This is a class method
    def say():
        print("Tomorrow!")

p1 = Person("Di", "Wang", 20)
print(p1.firstname)
print(p1.species)

# Class method called
Person.say()

# Another way of init an instance
p2 = Person()
Person.__init__(p2, "Di", "Wang", 20)
print(p2.firstname)
print(p2.surname)


