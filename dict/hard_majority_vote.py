"""
https://edabit.com/challenge/pQavNkBbdmvSMmx5x
"""

def majority_vote(lst):
    dict_a = dict()
    for i in lst:
        dict_a[i] = dict_a.get(i,0) + 1
    lst_length = len(lst)
    for k, v in dict_a.items():
        if v > lst_length / 2:
            return k

print(majority_vote(["A", "A", "A", "B", "C", "A"]) == "A")
print(majority_vote(["A", "B", "B", "A", "C", "C"]) == None)
