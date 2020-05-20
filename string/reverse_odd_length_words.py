"""
https://edabit.com/challenge/DjyqoxE3WYPe7qYCy
"""

"""
First solution using normal iteration
"""

def reverse_odd(txt):
    ans = ''
    temp = ''
    count = 0
    for i in range(len(txt)):
        if txt[i] != ' ':
            temp += txt[i]
            count += 1
        else:
            if len(temp) % 2 == 0:
                ans += temp + ' '
                temp = ''
            else:
                ans += temp[::-1] + ' '
                temp = ''
        if i == len(txt) - 1 and len(temp) != 0:
            if len(temp) % 2 == 0:
                ans += temp
            else:
                ans += temp[::-1]
    return ans
            
"""
Alternative solution generators and split
"""

##def reverse_odd(txt):
##    return  ' '.join(i if len(i) % 2 == 0 else i[::-1] for i in txt.split())

print(reverse_odd("One two three four") )
print(reverse_odd("One two three four") == "enO owt eerht four")
