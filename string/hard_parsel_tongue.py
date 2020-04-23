"""
https://edabit.com/challenge/uv6NvSydCGB7jKAyu
"""


def is_parsel_tongue(txt: str) -> bool:
    l = txt.split()
    for word in l:
        for i,v in enumerate(word):
            if i == len(word) - 1 and v in {'S', 's'}:
                return False
            elif v in {'S', 's'}:
                if word[i+1] in {'S', 's'}:
                    break
                else:
                    return False
    return True

"""
Alternative solution
"""


def is_parsel_tongue(sentence):
	return all('ss' in word or 's' not in word for word in sentence.lower().split())


assert is_parsel_tongue("Sshe ssselects to eat that apple.") == True
assert is_parsel_tongue("She ssselects to eat that apple.") == False
assert is_parsel_tongue("You ssseldom sssspeak sso boldly, ssso messmerizingly.") == True
assert is_parsel_tongue("Beatrice samples lemonade") == False
print('Success')