# You're given a variable json_course_data which is a JSON object that holds information about a ourse and the students in that course.

# Your task: Inside the get_scores function, return a list of all the student's scores on their first test. You can find the data you need in json_course_data

# Python code​​​​​​‌‌​​‌​‌​‌‌‌‌​​‌​‌‌​‌‌​‌​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False

import json

thestr = """
{
	"title":"Intermediate Python",
	"students": [
		{
			"name":"Nick",
			"scores": [
				56,
				73,
				68,
				84
			]
		},
		{
			"name":"Jane",
			"scores": [
				88,
				74,
				91,
				73
			]
		},
		{
			"name":"Mark",
			"scores": [
				93,
				66,
				52,
				33
			]
		}
	]
}
"""
json_course_data = json.loads(thestr)

def get_scores():
	first_test_scores = json_course_data
	return first_test_scores
	