"""
Consider a list (list = []). You can perform the following commands: 
insert i e: Insert integer at position
print: Print the list.
remove e: Delete the first occurrence of integer
append e: Insert integer at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of 
commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding 
operation on your list.
"""

if __name__ == '__main__':
    N = int(input())

ls = []
for i in range(N):
    x = input()
    y = x.split()
    if y[0] == "insert":
        ls.insert(int(y[1]), int(y[2]))
    elif y[0] == "append":
        ls.append(int(y[1]))
    elif y[0] == "remove":
        ls.remove(int(y[1]))
    elif y[0] == "reverse":
        ls.reverse()
    elif y[0] == "pop":
        ls.pop()
    elif y[0] == "sort":
        ls.sort()
    elif y[0] == "print":
        print(ls)

# Alternative solution using 'evval' 

# n = input()
# l = []
# for _ in range(n):
#     s = raw_input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print l