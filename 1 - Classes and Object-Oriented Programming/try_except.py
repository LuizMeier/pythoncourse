# print("before")

# try:
#     #4 / 0
#     print(age)

# except NameError as e:
#     print("This was a name issue")
#     print(e)

# except ZeroDivisionError:
#     print("Can't divide by 0")

# except Exception as e:
#     print("Some other error")

# class CheeseError(Exception):
#     pass

# def upper_fun(word):
#     if len(word) <= 0:
#         raise CheeseError("Word is empty!")
#     return word.upper()

# print(upper_fun(""))

# print("after")


# Challenge
print("before")

try:
    #4 / 0
    #print(age)

    print("1" + 1)

except NameError as e:
    print("This was a name issue")
    print(e)

except ZeroDivisionError:
    print("Can't divide by 0")

except Exception as e:
    print("Some other error")

