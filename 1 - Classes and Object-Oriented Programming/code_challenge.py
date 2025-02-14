# You're given a student class with a score property that is a list of scores from tests they have taken.

# Your task: create a method named average_score that returns the average of all their scores (you can do that by adding all the scores together and dividing by the numbers of scores they have.)

# Python code​​​​​​‌‌​​‌​‌​‌‌​​‌​​‌‌‌​​​‌‌​​ below
# Use print("messages...") to debug your solution.

show_expected_result = False

class Student:
    scores = [65,75,85,95]

    def average_score(self):
        # total = 0
        # for score in Student.scores:
        #     total += score
        #avg = total / len(Student.scores)
        avg = sum(self.scores) / len(self.scores)
        return avg