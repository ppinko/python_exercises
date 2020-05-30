"""
https://edabit.com/challenge/8xwqLZuTAsLpNSPEn
"""


def award_prizes(scores: dict) -> dict:
    medals = ['Gold', 'Silver', 'Bronze', 'Participation']
    awards = sorted(scores.values(), reverse=True)
    for key in scores:
        i = awards.index(scores[key])
        if i > 2:
            scores[key] = 'Participation'
        else:
            scores[key] = medals[i]
    return scores


""" Alternativer solution """

def award_prizes(names):
    awards = ['Gold', 'Silver', 'Bronze'] + ['Participation']*(len(names)-3)
    ranked = sorted(names, key=names.get, reverse=True)
    return dict(zip(ranked, awards))


assert award_prizes({'Joshua' : 45,'Alex' : 39,'Eric' : 43}) == \
       {'Joshua' : 'Gold','Alex' : 'Bronze','Eric' : 'Silver'}

assert award_prizes({'Person A' : 1,'Person B' : 2,'Person C' : 3,'Person D' : 4,'Person E' : 102}) == \
       {'Person A' : 'Participation','Person B' : 'Participation','Person C' : 'Bronze','Person D' : 'Silver','Person E' : 'Gold'}

assert award_prizes({'Mario' : 99,'Luigi' : 100,'Yoshi' : 299,'Toad' : 2}) == \
       {'Mario' : 'Bronze','Luigi' : 'Silver','Yoshi' : 'Gold','Toad' : 'Participation'}

print("Success")