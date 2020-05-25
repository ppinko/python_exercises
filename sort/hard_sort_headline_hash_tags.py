"""
https://edabit.com/challenge/DTqHDf3srwsCifC7j
"""


def get_hash_tags(txt: str) -> list:
    s = ''.join(i.lower() for i in txt if i.isalpha() or i.isspace())
    L = s.split()
    L.sort(key= len, reverse=True)
    return ['#' + i for i in L[:3]]


assert get_hash_tags("How the Avocado Became the Fruit of the Global Trade") == ["#avocado", "#became", "#global"]
assert get_hash_tags("Why You Will Probably Pay More for Your Christmas Tree This Year") == ["#christmas", "#probably", "#will"]
assert get_hash_tags("Hey Parents, Surprise, Fruit Juice Is Not Fruit") == ["#surprise", "#parents", "#fruit"]
assert get_hash_tags("Visualizing Science") == ["#visualizing", "#science"]
assert get_hash_tags("Minecraft Stars on Youtube Share Secrets to Their Fame") == ["#minecraft", "#youtube", "#secrets"]
assert get_hash_tags("Are You an Elite Entrepreneur?") == ["#entrepreneur", "#elite", "#are"]

print('Success')