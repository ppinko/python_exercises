"""
https://edabit.com/challenge/MKP8QxzuDaqYAJ6sZ
"""


def is_correct_aliases(names, aliases):
    return all(True if i.split()[0][0] == j.split()[0][0] and i.split()[0][0] == j.split()[1][0] else False
               for i, j in zip(names, aliases))



assert  is_correct_aliases(['Adrian M.', 'Harriet S.', 'Mandy T.'], ['Amazing Artichoke', 'Hopeful Hedgehog', 'Marvelous Mouse']) == True
assert  is_correct_aliases(['Rachel F.', 'Pam G.', 'Fred Z.', 'Nancy K.'], ['Reassuring Rat', 'Peaceful Panda', 'Fantastic Frog', 'Notable Nickel']) == True
assert  is_correct_aliases(['Beth T.'], ['Brandishing Mimosa']) == False
assert  is_correct_aliases(['Mick S.', 'Sam R.', 'Val W.'], ['Magnificent Mint', 'Sly Serpent', 'Victorious Viceroy']) == True
assert  is_correct_aliases(['Bella T.', 'Tom H.', 'Ben C.'], ['Beautiful Barn', 'Talented Tapestry', 'Cool Bamboo']) == False
assert  is_correct_aliases(['Bella T.', 'Tom H.', 'Ben C.'], ['Beautiful Barn', 'Talented Tapestry', 'Bountiful Bamboo']) == True

print('Success')