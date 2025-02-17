import pickle

age = [34, 434, 2323, 3354525253]

file = open("text.txt", "wb")
pickle.dump(age, file)
file.close()

file = open("text.txt", "rb")
new_age = pickle.load(file)
file.close()

print(new_age)