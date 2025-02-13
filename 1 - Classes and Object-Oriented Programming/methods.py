import random

class Dog:
    info = "A furry little creature"

    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1, 10)
        self.name = name

    def bark(self):
        print(f"Woof! My name is {self.name} and my number is {self.lucky_number}")

#print(Dog.info)

dog1 = Dog("Fido")
dog2 = Dog("Sarah")

dog1.bark()
dog2.bark()

# Challenge
class Table:
    info = "A piece of furniture"
    name = "Table"
    color = "Brown"

    # def __init__(self, sides):
    #     self.sides = sides
    #     print(f"My table has {self.sides} sides")

    def printSides(self):
        print(f"My table has {self.sides} sides")

myTable = Table()
myTable.sides = 4
myTable.printSides()