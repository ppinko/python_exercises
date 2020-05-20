"""
https://edabit.com/challenge/GmCW4ziDMvxqnxnAj
"""


def who_passed(students: dict) -> list:
    l = []
    for k, v in students.items():
        sub_l = []
        for i in v:
            if i[:i.index('/')] == i[i.index('/') + 1:]:
                sub_l.append(True)
            else:
                sub_l.append(False)
        if all(sub_l):
            l.append(k)
    return sorted(l)


""" Alternative solution """

def who_passed(students):
	return sorted([student for student, grades in students.items() if all(eval(grade)==1 for grade in grades)])


assert who_passed({
  "John" : ["5/5", "50/50", "10/10", "10/10"],
  "Sarah" : ["4/5", "50/50", "10/10", "10/10"],
  "Adam" : ["3/5", "46/50", "9/10", "10/10"],
  "Barry" : ["5/5", "50/50", "10/10", "10/10"]
}) == ["Barry", "John"]

assert who_passed({
  "Zara" : ["10/10"],
  "Kris" : ["10/10"],
  "Charlie" : ["10/10"],
  "Alex" : ["10/10"]
}) == ["Alex", "Charlie", "Kris", "Zara"]

print("Success")