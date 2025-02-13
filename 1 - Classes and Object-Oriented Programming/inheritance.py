import random

class Animal:
    info = "A living aorganism that feed on organic matter"

    def __init__(self, name):
        print("An animal is created")
        self.name = name

class Dog(Animal):
    info = "A furry little creature"

    def __init__(self, name):
        super().__init__(name)
        print("A dog is created")
        self.lucky_number = random.randint(1, 10)
        self.fur = ""


    def bark(self):
        print(f"Woof! My name is {self.name} and my number is {self.lucky_number}")

class Bulldog(Dog):
    
    def __init__(self, name):
        super().__init__(name)
        print("A bulldog is created")
        
dog1 = Bulldog("Fido")


# Challenge
class Table:

    def __init__(self, name, info, color):
        # info = "A piece of furniture"
        # name = "Table"
        # color = "Brown"
        print(f"A {name} is {info} and is {color}")

class Feet(Table):
        
        def __init__(self, name, info, color):
            super().__init__(name, info, color)

myTable = Feet("table", "piece of forniture", "brown")