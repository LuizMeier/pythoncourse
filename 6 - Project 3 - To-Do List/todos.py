import sys

file_name = "todo_data.txt"
todos = []

# Read File
try:
    file = open(file_name, "r")
    todos = file.readlines()
    file.close()
except:
    pass

#print(todos)

# Add Todo
if len(sys.argv) >= 3 and sys.argv[1].lower() == "add":
    todos.append(f"{sys.argv[2]}\n")

# Remove Todo
if len(sys.argv) >= 3 and sys.argv[1].lower() == "remove":
    try:
        index_to_delete = int(sys.argv[2])
        if index_to_delete > 0:
            index_to_delete -= 1
            del(todos[index_to_delete])
        else:
            print("Index must be greater than 0!")
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

#print(todos)

# Save File
file = open(file_name, "w")
file.writelines(todos)
file.close()

# Print List
if len(todos) == 0:
    print("You have no ToDos!")
else:
    print("\nHere's your ToDo list:\n")
    for x in range(len(todos)):
        print(f"{x+1}) {todos[x]}", end="")

# Print Commands
print("\n**************************\n")
print(f"To view ToDos:\n{sys.argv[0]}")
print(f"To add a ToDo:\n{sys.argv[0]} add \"Clean Room\"\n")
print(f"To remove or complete ToDo:\n{sys.argv[0]} remove 2\n")