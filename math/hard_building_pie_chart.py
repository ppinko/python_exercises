"""
https://edabit.com/challenge/GwCAximybWF6ANdLY
"""

def pie_chart(d: dict) -> dict:
    temp = sum(d.values())
    return { k: round(v*360/temp,1) for k,v in d.items()} 

assert pie_chart({"a": 8, "b": 21, "c": 12, "d": 5, "e": 4}) == {"a": 57.6, "b": 151.2, "c": 86.4, "d": 36, "e": 28.8}
assert pie_chart({"a": 30, "b": 15, "c": 55}) == {"a": 108, "b": 54, "c": 198}
assert pie_chart({"a": 1, "b": 2}) == {"a": 120, "b": 240}

print("Success")
