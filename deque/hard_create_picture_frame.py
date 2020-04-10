"""
https://edabit.com/challenge/wEr6R9kc5oG88FRYy
"""
"""
Solution using deque
"""

##from collections import deque
##
##def get_frame(w, h, ch):
##    if w <= 2 or h <= 2:
##        return "invalid"
##    d = deque()
##    for i in range(h-2):
##        d.append(ch + (w-2) * ' ' + ch)
##    d.appendleft(ch * w)
##    d.append(ch * w)
##    return list(d)
##

"""
Solution using list
"""

def get_frame(w, h, ch):
    if w <= 2 or h <= 2:
        return "invalid"
    l = []
    for i in range(h-2):
        l.append([ch + (w-2) * ' ' + ch])
    l.insert(0, [ch * w])
    l.append([ch * w])
    return l

for i in get_frame(4, 5, "#"):
    print(i)

print(get_frame(2, 5, "0") == "invalid")
