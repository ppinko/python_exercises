"""
Sample Input:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output:
4
"""

n = int( input() )
setA = set(input().split())
operations = int( input() )

for i in range(operations):
    oper = input()
    if oper == 'pop':
        eval('{0}.{1}()'.format('setA', oper))
    else:
        oper_ls = oper.split()
        # print('{0}.{1}("{2}")'.format('setA', oper_ls[0], oper_ls[1]))
        eval('{0}.{1}("{2}")'.format('setA', oper_ls[0], oper_ls[1]))
    print(setA)
print(len(setA))

# ALTERNATIVE SOLUTION
n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))