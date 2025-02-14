age = 9
height = 100

# and
if age >= 8 and height >=135:
    print("You can ride the roller coaster!")

# or
if age >= 17 or height >= 160:
    print("You can ride the super ride!")

# elif (else if)
if height < 120:
    print("You can't ride any rides :(")
elif height < 135:
    print("You can ride the baby ride!")
elif height < 200:
    print("You can ride any ride!")
else:
    print("Tool tall to ride the rides :(")

# challenge
if age > 18 and (height > 120 or height < 200):
    print("You can ride the roller coaster!")