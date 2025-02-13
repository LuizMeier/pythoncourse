import random

class Dog:
    info = "A furry little creature"

    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1, 10)
        self.name = name

#print(Dog.info)

dog1 = Dog("Fido")
dog2 = Dog("Sarah")

print(dog1.name)
print(dog2.name)


# Challenge
class Table:
    info = "A piece of furniture"
    name = "Table"
    color = "Brown"

print(Table.info)

my_table = Table()
Table.sides = 4

print(Table.sides)