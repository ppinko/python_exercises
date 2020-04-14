"""
https://edabit.com/challenge/jwzAdBnJnBxCe4AXP
"""

def rearranged_difference(n):
    l1 = sorted(list(str(n)), reverse=True)
    l2 = sorted(list(str(n)))
    s1 = ''
    s2 = ''
    for i in l1:
        s1 += i
    for j in l2:
        s2 += j
    return int(s1) - int(s2)

"""
Alternative solution
"""
def rearranged_difference(num):
	n = ''.join(sorted(str(num)))
	return int(n[::-1]) - int(n)

assert rearranged_difference(9092564) == 9719721
assert rearranged_difference(1308821) == 8719722
assert rearranged_difference(8386568) == 5319765
assert rearranged_difference(7794084) == 9429651
assert rearranged_difference(6366093) == 9329661
assert rearranged_difference(7863060) == 8729622
assert rearranged_difference(3368327) == 6429654
assert rearranged_difference(7218787) == 7599933
assert rearranged_difference(7723188) == 7639533
assert rearranged_difference(8816317) == 7739523
assert rearranged_difference(8824349) == 7539543
assert rearranged_difference(3320707) == 7709823
assert rearranged_difference(1695488) == 8429652
assert rearranged_difference(2120034) == 4309866
assert rearranged_difference(5300586) == 8619732
assert rearranged_difference(3538814) == 7519743
assert rearranged_difference(1336939) == 8629632
assert rearranged_difference(6290200) == 9619731
assert rearranged_difference(5268866) == 6299964
assert rearranged_difference(5155458) == 7099983

print("Success")
