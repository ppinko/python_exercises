"""
Question 19
Level 3

Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order 
where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""

def sort_list(ls):
    sort_list = []
    sort_list.append(ls[0])
    for i in ls[1:]:
        for j in range(len(sort_list)):
            if i[0] < sort_list[j][0]:
                sort_list.insert(j, i)
                break
            elif i[0] == sort_list[j][0]:
                if i[1] < sort_list[j][1]:
                    sort_list.insert(j, i)
                    break
                elif i[1] == sort_list[j][1]:
                    if i[2] < sort_list[j][2]:
                        sort_list.insert(j, i)
                        break
            elif j == (len(sort_list)) - 1:
                sort_list.insert(j, i)
                break
    return sort_list

ls_names = [[["Tom"],[19],[80]], [["John"],[20],[90]], [["Jony"],[17],[91]], [["Jony"],[17],[93]], [["Json"],[21],[85]]]

print(sort_list(ls_names))

"""
from operator import itemgetter, attrgetter

ALTERNATIVE SOLUTION
l = []
while True:
    s = raw_input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print sorted(l, key=itemgetter(0,1,2))
"""