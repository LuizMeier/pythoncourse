# # Creates only if the file does not exist
# file = open("cheese.txt", "x")

# file.write("X marks the spot!")

# file.close()


# # Overwrite the file
# file = open("cheese.txt", "w")

# file.write("For the W!")

# file.close()

# # Append to the file
# file = open("cheese.txt", "a")

# file.write("A+ work!")

# file.close()


# Challenge

# Create a file named after an argument passed to the script
import sys
del(sys.argv[0])
for argument in sys.argv:
    file = open(argument, "x")
    file.write("This file name came from an argument!")
    file.close()
