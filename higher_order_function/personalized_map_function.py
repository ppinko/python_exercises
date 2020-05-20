def my_map(func, ls):
    l = []
    for i in ls:
        l.append(func(i))
    return l

def half(n):
    return n/2

l = [1, 3, 4, 7]
letters = ['a', 'c', 'd']

print(my_map(half, l))

print(my_map(str.lower, letters))

print(list(map(str.lower, letters)))
