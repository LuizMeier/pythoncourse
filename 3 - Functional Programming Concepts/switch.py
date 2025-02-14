# Requires Python 3.10

direction = input("Which direction? ").lower()

match direction:
    case "north":
        print("Up")
    case "south":
        print("Down")
    case "east":
        print("Right")
    case "west":
        print("Left")
    case _:
        print("Unknown direction")

# Challenge
floor = input("Which floor? ").lower()

match floor:
    case "13":
        print("Unlucky in US")
    case "4":
        print("Unlucky in China")
    case _:
        print("Lucky floor")