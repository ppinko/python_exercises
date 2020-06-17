# https://edabit.com/challenge/r7kZBzW3si9rJrLXh


import string

def get_sentence_value(txt):
    txt = ''.join(i for i in txt if i.isalpha() or i == ' ')
    if txt.strip() == '':
        return 0
    tot = 0
    d_letters = dict(zip(string.ascii_lowercase, range(1, len(string.ascii_lowercase) + 1)))
    for i in txt.split():
        flag = all(True if j.isupper() else False for j in i)
        word = 0
        for w in i:
            if w.lower() in d_letters:
                word += d_letters[w.lower()]
        if flag:
            word *= 2
        tot += word
    return tot



assert get_sentence_value("abc ABC Abc") == 24
assert get_sentence_value("HELLO world") == 176
assert get_sentence_value("Edabit is Legendary") == 160
assert get_sentence_value("Her seaside sea-shelling business is really booming!") == 488
assert get_sentence_value("edabit Edabit EDABIT") == 164
assert get_sentence_value("expensive words") == 198
assert get_sentence_value("FISH AND CHIPS") == 232
assert get_sentence_value("this sentence is like a piece of hay in a needle stack") == 423
assert get_sentence_value("CAN YOU STOP SHOUTING?! I CAN'T HEAR MYSELF THINK!!!") == 966
assert get_sentence_value("a whisper in the wind...") == 205
assert get_sentence_value(",.;[,.;][,.;[,.][,.;,.][") == 0
assert get_sentence_value("Isn't it funny how the word BIG is physically smaller than the word small?") == 777
assert get_sentence_value("this is a really pricey sentence: ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ") == 2503
assert get_sentence_value("                    ") == 0
assert get_sentence_value("") == 0
assert get_sentence_value("Oranges and APPLES") == 236
assert get_sentence_value("Edabit is LEGENDARY") == 251

print("Success")