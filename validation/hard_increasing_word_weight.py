"""
https://edabit.com/challenge/f6X7pa38iQyoytJgr
"""


def increasing_word_weights(txt: str) -> bool:
    from functools import reduce
    temp = []
    for i in txt.split():
        temp_points = 0
        for j in i:
            if j.isalpha():
                temp_points += ord(j)
        if temp_points != 0:
            temp.append(temp_points)
    return temp == sorted(temp)



assert increasing_word_weights("Why not try?") == True
assert increasing_word_weights("Face your fears == never settle.") == True
assert increasing_word_weights("DON'T SHOUT!") == True
assert increasing_word_weights("Can you just leave?") == True
assert increasing_word_weights("You will push ahead == creating solutions!") == True
assert increasing_word_weights("All that money doesn't guarantee happiness.") == True
assert increasing_word_weights("Full steam ahead!") == False
assert increasing_word_weights("Not all those who wander are lost.") == False
assert increasing_word_weights("All other roads.") == False
assert increasing_word_weights("Whatever you are == be a good one.") == False
assert increasing_word_weights("Standing on the shoulders of giants.") == False
assert increasing_word_weights("You get what you settle for.") == False

print('Success')