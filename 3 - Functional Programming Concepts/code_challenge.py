# Return a list of students who's name starts with the letter "M". Be sure to use filter to do this

# Python code​​​​​​‌‌​​‌​‌‌​​​​‌​​​‌​​​‌‌​​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False

class Student:
	def __init__(self, name, score):
		self.name = name
		self.score = score
	
	def __repr__(self): 
		return f"{self.name}: {self.score}"
	
students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63), Student("Mary", 0.55)]



def m_students():
	filter_list = list(filter(lambda student: student.name.startswith("M"), students ))
	return filter_list