"""
https://edabit.com/challenge/ofuahH9E4pcRDNChd
"""


def rpn(lst: list) -> int:
    L = []
    for i in lst:
        if type(i) != int:
            if i == '+':
                L[-2] = L[-2] + L[-1]
            elif i == '-':
                L[-2] = L[-2] - L[-1]
            elif i == '*':
                L[-2] = L[-2] * L[-1]
            else:
                L[-2] = L[-2] // L[-1]
            L.pop()
        else:
            L.append(i)
    return L[-1]


assert rpn([1,2,'*',4,5,'*','+']) ==22
assert rpn([1,1,'+']) ==2
assert rpn([16,16,'/']) ==1
assert rpn([7,6,'-']) ==1
assert rpn([1,2,3,4,5,6,'+','+','+','+','+']) ==21
assert rpn([1]) ==1
assert rpn([12345,12344,'-']) ==1
assert rpn([1,7,'*']) ==7
assert rpn([1,5,'+',2,'/']) ==3
assert rpn([111,222,'+',333,'-']) ==0
assert rpn([1,2,'-']) ==-1
assert rpn([1,1,'/',2,'+',2,'*',3,'/']) ==2
assert rpn([9,9,'*',6,6,'*','-',9,'/']) ==5
assert rpn([15,15,'*']) ==225
assert rpn([1,1,1,1,1,1,'+','+','+','+','+']) ==6

print('Success')