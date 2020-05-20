"""
https://edabit.com/challenge/ivWdkjsHtKSMZuNEc
"""


def find_shortest_words(txt: str) -> list:
    txt = txt.strip('.')
    temp = sorted(txt.split(), key=len)
    l = [temp[0].lower()]
    for i in temp[1:]:
        if len(i) == len(l[0]):
            if i.isalpha():
                l.append(i.lower())
        else:
            break
    return sorted(l)


assert find_shortest_words("Strive not to be a success, but rather to be of value.") == ['a']
assert find_shortest_words("You miss 100% of the shots you don't take.") == ['of']
assert find_shortest_words("Life is what happens to you while you're busy making other plans.") == ['is', 'to']
assert find_shortest_words("We become what we think about.") == ['we', 'we']
assert find_shortest_words("The most common way people give up their power is by thinking they don't have any.") == ['by', 'is', 'up']
assert find_shortest_words("The best time to plant the tree was 20 years ago. The second best time is now.") == ['is', 'to']
assert find_shortest_words("Your time is limited, so don't waste it living someone else's life.") == ['is', 'it', 'so']
assert find_shortest_words("You can never cross the ocean until you have the courage to lose sight of the shore.") == ['of', 'to']
assert find_shortest_words("There is only one way to avoid criticism: do nothing, say nothing, and be nothing.") == ['be', 'do', 'is', 'to' ]
assert find_shortest_words("The only person you are destined to become is the person you decide to be.") == ['be', 'is', 'to', 'to']
assert find_shortest_words("What lies behind us and what lies before us are tiny matters compared to what lies within us.") == ['to', 'us', 'us', 'us']
assert find_shortest_words("If you are depressed you are living in the past. If you are anxious you are living in the future. If you are at peace you are living in the present.") == ['at', 'if', 'if', 'if', 'in', 'in', 'in']
assert find_shortest_words("Happiness depends upon ourselves.") == ['upon']
assert find_shortest_words("Chase two rabbits, catch none.") == ['two']
assert find_shortest_words("Only the truth of who you are, if realized, will set you free.") == ['if', 'of']
assert find_shortest_words("If you end up with a boring miserable life because you listened to your parents, your teacher, your priest, or some guy on television, then you deserve it.") == ['a']
assert find_shortest_words("To accomplish great things, we must not only act, but also dream; not only plan, but also believe.") == ['to', 'we']
assert find_shortest_words("A tiger doesn't lose sleep over the opinion of sheep.") == ['a']
assert find_shortest_words("Kindness is a language that the deaf can hear and the blind can see.") == ['a']
assert find_shortest_words("Being realistic is the most common path to mediocrity.") == ['is', 'to']
assert find_shortest_words("Bravery means finding something more important than fear.") == ['fear', 'more', 'than']
assert find_shortest_words("Can you imagine what I would do if I could do all I can?") == ['i', 'i', 'i']
assert find_shortest_words("Believe you can and you're halfway there.") == ['and', 'can', 'you']
assert find_shortest_words("Remember that happiness is a way of travel, not a destination.") == ['a', 'a']
assert find_shortest_words("May the best day of your past be the worst day of your future.") == ['be', 'of', 'of']

print('Success')