class Student:
    def __init__(self, name, score):
        self.score = score
        self.name = name

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.92)]

student_results = []

for student in students:
    # if student.score >= 0.7:
    #     student_results.append(f"{student.name} Passed")
    # else:
    #     student_results.append(f"{student.name} Failed")


    student_results.append(f"{student.name} Passed") if student.score >= 0.7 else student_results.append(f"{student.name} Failed")

map_results = list(map(lambda student: f"{student.name} Passed" if student.score >= 0.7 else f"{student.name} Failed", students))

print(map_results)


# Challenge
# Use map to multiply all these numbers by 2

numbers = [1, 2, 3, 4, 5]

map_results = list(map(lambda number: number * 2, numbers))

print(map_results)