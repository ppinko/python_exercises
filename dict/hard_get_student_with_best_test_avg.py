"""
https://edabit.com/challenge/pnd7xPYuvogkNfHg6
"""


def get_best_student(students: dict) -> str:
    l = [(k, sum(v)/len(v)) for k, v in students.items()]
    l.sort(key=lambda x: x[1], reverse=True)
    return l[0][0]


assert get_best_student({
	"John": [100, 90, 80],
	"Bob": [100, 70, 80]
}) == "John"

assert get_best_student({
	"Susan": [67, 84, 75, 63],
  "Mike": [87, 98, 64, 71],
  "Jim": [90, 58, 73, 86]
}) == "Mike"

print("Success")