"""
https://edabit.com/challenge/WpRhk6tKJFmvJA6cq
"""


from datetime import timedelta


class Train:
    def __init__(self, destinations, expected_time):
        self.destinations = destinations
        self.expected_time = expected_time

def manage_delays(train, dest, delay):
    if dest in train.destinations:
        L = [int(i) for i in train.expected_time.split(':')]
        t_init = timedelta(hours=L[0], minutes=L[1])
        t_add = timedelta(minutes=delay)
        t = t_init + t_add
        train.expected_time = str(t)[:5]


trains = [
    Train(['Townsville', 'Suburbia', 'Urbantska'], '13:04'),
    Train(['Farmsdale', 'Suburbia', 'Lakeside Valley'], '13:20'),
    Train(['Suburbia', 'Townsville', 'Lakeside Valley'], '13:22')
]

for t in trains:
    manage_delays(t, 'Lakeside Valley', 60)

assert trains[0].expected_time == '13:04'
assert trains[1].expected_time == '14:20'
assert trains[2].expected_time == '14:22'

for t in trains:
    manage_delays(t, 'Farmsdale', 20)

assert trains[0].expected_time == '13:04'
assert trains[1].expected_time == '14:40'
assert trains[2].expected_time == '14:22'

for t in trains:
    manage_delays(t, 'Townsville', 100)

assert trains[0].expected_time == '14:44'
assert trains[1].expected_time == '14:40'
assert trains[2].expected_time == '16:02'