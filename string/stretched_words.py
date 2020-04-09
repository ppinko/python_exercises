"""
https://edabit.com/challenge/fmQ9QvPBWL7N9hSkq
"""

def unstretch(word):
    unstretched = word[0]
    for i in range(1, len(word)):
        if word[i] != word[i-1]:
            unstretched += word[i]
    return unstretched

"""
Alternative solution - using generator
"""

##def unstretch(word):
##    return word[0] + ''.join(word[i] for i in range(1,len(word)) if word[i] != word[i-1])

"""
Alternative solution - using generator + zip
"""
##def unstretch(word):
##    return ''.join([x for x,y in zip(word,word[1:]) if x!=y]) + word[-1]

print(unstretch("ttiiitllleeee"))
print(unstretch("ttiiitllleeee") == "title")
